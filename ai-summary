#!/usr/bin/env python3
"""
Complete report generation pipeline:
1. (Optional) Run analyzer-script to generate analysis data
2. Upload analysis JSON to GitHub Gist
3. Call DeepSeek API to generate new bilingual reports
"""

import os
import sys
import json
import argparse
import subprocess
import re
from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI

# ---------- Argument parsing ----------
def parse_args():
    parser = argparse.ArgumentParser(description="Automated telemetry report generator")
    parser.add_argument("--report-id", required=True,
                        help="Report ID in format XXXXXXXX_A (8 digits, underscore, lowercase letter)")
    parser.add_argument("--last-report-id", required=True,
                        help="Previous report ID, same format")
    parser.add_argument("--workers", type=int, default=150,
                        help="Number of parallel workers for analyzer-script (default: 150)")
    parser.add_argument("--log-level", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                        help="Log level (default: INFO)")
    parser.add_argument("--from", dest="from_date", required=True,
                        help="Start date in YYYY/MM/DD format")
    parser.add_argument("--to", dest="to_date", required=True,
                        help="End date in YYYY/MM/DD format")
    parser.add_argument("--skip-analysis", action="store_true",
                        help="Skip running analyzer-script; use existing analysis JSON file")
    parser.add_argument("--extra-focus", type=str, default="",
                        help="Extra dimensions or metrics to pay special attention to in the report")
    return parser.parse_args()

# ---------- Helper functions ----------
def validate_report_id(rid: str) -> None:
    """Validate format: 8 digits + underscore + single lowercase letter"""
    if not re.fullmatch(r'[0-9]{8}_[a-z]', rid):
        raise ValueError(f"Invalid report-id format: {rid}, expected 8 digits _ lowercase letter")

def get_report_dir(rid: str) -> Path:
    """
    Build report directory path from report-id.
    e.g. 20260801_a -> reports/2026/08/01_a/
    """
    digits, letter = rid.split('_')
    if len(digits) != 8:
        raise ValueError(f"Digits part must be 8 characters: {rid}")
    sub1, sub2, sub3 = digits[0:4], digits[4:6], digits[6:8]
    last_dir = f"{sub3}_{letter}"
    return Path("reports") / sub1 / sub2 / last_dir

def read_file(path: Path) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def strip_think_tags(text: str) -> str:
    """Remove <think>...</think> blocks from the response."""
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

def extract_json_from_response(text: str) -> dict:
    """
    Extract JSON from text that may contain markdown fences or think tags.
    """
    # Remove <think> tags
    text = strip_think_tags(text)
    # Strip markdown code fences
    if '```' in text:
        lines = text.split('\n')
        in_code = False
        json_lines = []
        for line in lines:
            if line.strip().startswith('```'):
                in_code = not in_code
                continue
            if in_code:
                json_lines.append(line)
        text = '\n'.join(json_lines)
    # Try to parse as JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # If still not valid, try to find first { ... } block
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise

# ---------- Main ----------
def main():
    args = parse_args()
    report_id = args.report_id
    last_report_id = args.last_report_id
    validate_report_id(report_id)
    validate_report_id(last_report_id)

    # Determine analysis file path
    analysis_path = Path(f"internal_stats/analysis-{report_id}.json")

    # 1. Run analyzer-script unless skipped
    if not args.skip_analysis:
        venv_python = Path(".venv/bin/python")
        if not venv_python.exists():
            print("Error: virtual environment (.venv) not found", file=sys.stderr)
            sys.exit(1)

        cmd = [
            str(venv_python), "-m", "analyzer-script",
            "-w", str(args.workers),
            "--log-level", args.log_level,
            "--from", args.from_date,
            "--to", args.to_date,
            "-d", f"internal_stats/data-{report_id}.zip",
            "-a", str(analysis_path)
        ]
        print(f"Executing: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            print("analyzer-script failed:", file=sys.stderr)
            print(proc.stderr, file=sys.stderr)
            sys.exit(proc.returncode)
        print("analyzer-script finished successfully")
    else:
        print("Skipping analyzer-script as requested")

    # Verify analysis file exists
    if not analysis_path.exists():
        print(f"Error: analysis file {analysis_path} not found", file=sys.stderr)
        sys.exit(1)

    # 2. Load credentials from .summary.env
    env_path = Path(".summary.env")
    if not env_path.exists():
        print("Error: .summary.env not found", file=sys.stderr)
        sys.exit(1)
    load_dotenv(env_path)
    github_token = os.getenv("GITHUB_TOKEN")
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    if not github_token:
        print("Error: GITHUB_TOKEN not set in .summary.env", file=sys.stderr)
        sys.exit(1)
    if not deepseek_key:
        print("Error: DEEPSEEK_API_KEY not set in .summary.env", file=sys.stderr)
        sys.exit(1)

    # 3. Upload analysis JSON to Gist
    with open(analysis_path, 'r', encoding='utf-8') as f:
        analysis_data = f.read()

    gist_payload = {
        "description": "LangPatch Telemetry Analysis Data",
        "public": False,
        "files": {
            "data_analysis.json": {
                "content": analysis_data
            }
        }
    }
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    print("Uploading to GitHub Gist ...")
    resp = requests.post("https://api.github.com/gists", json=gist_payload, headers=headers)
    if resp.status_code != 201:
        print(f"Gist upload failed (HTTP {resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)
    gist_data = resp.json()
    gist_url = gist_data["html_url"]
    print(f"Gist uploaded: {gist_url}")

    # 4. Read previous reports
    last_dir = get_report_dir(last_report_id)
    en_old_path = last_dir / "en.md"
    zh_old_path = last_dir / "zh.md"
    if not en_old_path.exists() or not zh_old_path.exists():
        print(f"Error: previous report files missing: {en_old_path} or {zh_old_path}", file=sys.stderr)
        sys.exit(1)
    en_old = read_file(en_old_path)
    zh_old = read_file(zh_old_path)

    # 5. Prepare output directory for current report
    report_dir = get_report_dir(report_id)
    report_dir.mkdir(parents=True, exist_ok=True)
    en_new_path = report_dir / "en.md"
    zh_new_path = report_dir / "zh.md"

    # 6. Build prompt with optional extra focus
    extra_focus_text = ""
    if args.extra_focus:
        extra_focus_text = f"""
**Extra dimensions to focus on**
The following additional metrics or dimensions should be highlighted and analyzed in detail:
{args.extra_focus}
"""
    prompt = f"""
You are a professional telemetry report writer. Based on the data provided, generate a new bilingual report.
Telemetry date range: from {args.from_date} to {args.to_date}

**Raw analysis data (JSON)** has been uploaded to GitHub Gist at: {gist_url}
Below is the full JSON content for your direct analysis.

--- Analysis data (analysis-{report_id}.json) start ---
{analysis_data}
--- Analysis data end ---

**Previous report (for style and content reference)**
--- English version start ---
{en_old}
--- English version end ---

--- Chinese version start ---
{zh_old}
--- Chinese version end ---

{extra_focus_text}

**Task requirements**
- Write a new telemetry report based on the analysis data, covering data summary, key findings, trends, etc.
- Produce both English and Chinese versions; language must be fluent, professional, and well-structured.
- **Output format**: Must return a valid JSON object with two fields:
  - "english": full English report in Markdown (string)
  - "chinese": full Chinese report in Markdown (string)
- In the report, mention that the raw data is accessible via the Gist link: {gist_url}.
- If extra focus dimensions are provided, ensure they receive dedicated attention and analysis.

Output strictly in JSON format, no extra text.
"""

    # 7. Call DeepSeek API to generate new reports
    print("Calling DeepSeek API ...")
    client = OpenAI(
        api_key=deepseek_key,
        base_url="https://api.deepseek.com"   # Official endpoint
    )

    try:
        # Use deepseek-chat (or deepseek-v4-pro if available)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional data analysis report writer. Output only JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=8192,
        )

        # Debug info
        print(f"Response finish_reason: {response.choices[0].finish_reason}")
        if not response.choices:
            print("Error: No choices returned.", file=sys.stderr)
            sys.exit(1)

        result_text = response.choices[0].message.content
        if not result_text:
            print("Error: Received empty content from API.", file=sys.stderr)
            if response.choices[0].finish_reason == 'length':
                print("Hint: max_tokens may be too small.", file=sys.stderr)
            elif response.choices[0].finish_reason == 'content_filter':
                print("Hint: Content was filtered by safety policy.", file=sys.stderr)
            sys.exit(1)

        print(f"Raw response (first 500 chars):\n{result_text[:500]}")

        # Parse JSON (handle think tags and markdown)
        data = extract_json_from_response(result_text)
        en_new = data.get('english', '').strip()
        zh_new = data.get('chinese', '').strip()
        if not en_new or not zh_new:
            raise ValueError("Missing 'english' or 'chinese' field in response")

    except Exception as e:
        print(f"DeepSeek API call or parsing failed: {e}", file=sys.stderr)
        if 'result_text' in locals():
            print(f"Full response:\n{result_text}", file=sys.stderr)
        sys.exit(1)

    # 8. Write new reports
    write_file(en_new_path, en_new)
    write_file(zh_new_path, zh_new)
    print(f"Reports generated successfully:\n  - {en_new_path}\n  - {zh_new_path}")
    print(f"Analysis Gist URL: {gist_url}")

if __name__ == "__main__":
    main()