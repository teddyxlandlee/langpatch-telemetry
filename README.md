# LangPatch Telemetry

This repository contains the source code for the telemetry/reporting system used by [Enchantment Level Language Patch](https://modrinth.com/mod/enchlevel-langpatch).

It is primarily responsible for:

- collecting and presenting telemetry reports
- generating a report index for front-end consumption
- implementing Netlify relay logic and OSS storage integration
- supporting offline and online telemetry analysis

## Repository structure

- `gen_report_list.cjs`
  - scans `./reports/` for report folders matching the `a/b/c` pattern that contain `en.md` and `zh.md`
  - generates `reports.json` for static web pages and front-end use
- `reports/`
  - contains generated telemetry snapshot reports, including English and Chinese versions
- `reports.html`, `browse.html`
  - static report browser entry pages
- `netlify/`
  - `edge-functions/telemetry.js`: Edge/front-end entrypoint that receives telemetry requests and forwards them
  - `functions/telemetry-impl.js`: Netlify function relay logic that invokes cloud storage SDKs
- `analyzer-script/`
  - Python analysis scripts for fetching telemetry data from cloud storage and generating analytics output
- `internal_stats/`
  - excluded by `.gitignore`, where you can store internal analysis artifacts
- `PRIVACY.md`
  - telemetry privacy policy
- `SCHEMA.txt`
  - telemetry data schema description

## Dependencies and installation

### Node.js side

```bash
npm install
```

Running `npm install` triggers the `postinstall` script:

```bash
node gen_report_list.cjs
```

This generates `reports.json` so the static front-end can read the available report list.

### Python analysis side

The Python analysis scripts depend on `analyzer-script/requirements.txt`:

- `alibabacloud-oss-v2`
- `cos_python_sdk_v5`
- `dotenv`

Recommended setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r analyzer-script/requirements.txt
```

## Usage

### Generate report index

```bash
node gen_report_list.cjs
```

This scans the `reports/` directory and writes `reports.json`.

### Analyze telemetry data

The Python script entrypoint is `analyzer-script/__main__.py`.

#### 1. Configure cloud storage credentials

Create a `.env` file under `internal_stats/` with content similar to:

```ini
BUCKET_PROVIDER=aliyun
BUCKET_NAME=...
BUCKET_REGION=...
BUCKET_ACCESS_KEY_ID=...
BUCKET_ACCESS_KEY_SECRET=...
```

Or for Tencent:

```ini
BUCKET_PROVIDER=tencent
BUCKET_NAME=...
BUCKET_REGION=...
BUCKET_ACCESS_KEY_ID=...
BUCKET_ACCESS_KEY_SECRET=...
```

#### 2. Run analysis

Fetch data from remote storage and analyze it:

```bash
python -m analyzer-script --from 2026/05/01 --to 2026/05/25 -d data.zip -a analysis.json
```

Analyze existing local data only:

```bash
python -m analyzer-script -i path/to/data_folder -a analysis.json
```

## Privacy and data policy

This repository's telemetry system follows the policy described in `PRIVACY.md`:

- no username, UUID, or IP address is collected
- telemetry is sent only with user consent
- supports data levels: `Necessary (0)`, `Functional (1)`, `Optional (2)`, and `Disabled (-1)`
- Netlify Functions are used as a relay and do not store telemetry data
- final data is written to Alibaba Cloud OSS, with the default region set to `oss-cn-shanghai`

## Maintenance

This repository is mainly for internal maintenance and deployment. When modifying telemetry flow or report generation logic, start by reviewing:

- `gen_report_list.cjs`
- `netlify/edge-functions/telemetry.js`
- `netlify/functions/telemetry-impl.js`
- `analyzer-script/__main__.py`
- `analyzer-script/dstat_v2.py`
- `PRIVACY.md`

## License

This repository is licensed under the terms in `LICENSE`.
