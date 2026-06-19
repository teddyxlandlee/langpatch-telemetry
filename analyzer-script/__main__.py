import argparse
import os
import re
import sys
import zipfile
from datetime import datetime, timezone as _timezone, timedelta
from .dstat_v2 import *
from .bucket_spec import RemoteBucket, RemoteBucketConstructor

try:
    from dotenv import load_dotenv
except ImportError:
    if __name__ == '__main__':
        print('Error: dotenv not found. Please configure venv first.')
        sys.exit(-1)
    else:
        raise

# Please place a .env file in the internal_stats folder.
# See .env.example for reference. The internal_stats folder is ignored by git to avoid leaking credentials.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(sys.argv[0]), '..', 'internal_stats', '.env'))

# === Default implementations ===
ACCESS_KEY_ID = os.getenv('BUCKET_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('BUCKET_ACCESS_KEY_SECRET')
BUCKET_NAME = os.getenv('BUCKET_NAME')
BUCKET_REGION = os.getenv('BUCKET_REGION')
# =============

def connect_to_remote_storage(max_workers: int = 10) -> RemoteBucket:
    ctr: RemoteBucketConstructor
    match os.getenv('BUCKET_PROVIDER', '').lower():
        case 'aliyun':
            from .bucket_aliyun import AliyunBucket
            ctr = AliyunBucket
        case 'tencent':
            from .bucket_tencent import TencentBucket
            ctr = TencentBucket
        case _:
            raise NotImplementedError('Unsupported bucket provider: ' + os.getenv('BUCKET_PROVIDER', '<unknown>'))
    return ctr(
        bucket_name=BUCKET_NAME,
        access_key_id=ACCESS_KEY_ID,
        access_key_secret=ACCESS_KEY_SECRET,
        region=BUCKET_REGION,
        max_workers=max_workers,
    )

def main(start_date: str, end_date: str, zip_output: str, analysis_output: str, max_workers: int):
    assert re.match('^\\d{4}/\\d{2}/\\d{2}', start_date), 'Illegal start_date'
    assert re.match('^\\d{4}/\\d{2}/\\d{2}', end_date), 'Illegal end_date'
    date_prefixes = date_range(start_date, end_date)

    logging.info(f'Fetching {start_date} -> {end_date} ({len(date_prefixes)} day(s))')
    
    remote_bucket = connect_to_remote_storage(max_workers=max_workers)
    fetched = fetch_files(date_prefixes, remote_bucket, max_workers)
    # Eagerly load all files to memory (meanwhile filter fails)
    filtered: dict[str, dict] = {}
    errors = []
    for item in fetched:
        status = item.get('status', 'fail')
        if status == 'success':
            filtered[item['key']] = item['data']
        else:
            errors.append(item.get('error'))
    if errors:
        logging.warning(f'Found {len(errors)} corrupted data.')
        for count, err in enumerate(errors):
            logging.warning(f'- {count + 1}. {err}')
    
    with zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for k, v in filtered.items():
            zf.writestr(k, json.dumps(v, indent=2))
    
    analysis = analyze_data(filtered)
    with open(analysis_output, 'w', encoding='utf8') as f:
        json.dump(analysis, f, indent=2)

def main_analyze_only(zip_or_folder_input: str, analysis_output: str):
    data_input: dict[str, dict] = {}
    if zipfile.is_zipfile(zip_or_folder_input):
        with zipfile.ZipFile(zip_or_folder_input) as zf:
            for entry in (x for x in zf.infolist() if (not x.is_dir()) and x.filename.endswith('.json')):
                with zf.open(entry) as f:
                    data_input[entry.filename] = json.load(f)
    elif os.path.isdir(zip_or_folder_input):
        for path in (
            os.path.join(folder, fn)
              for folder, _, filenames in os.walk(zip_or_folder_input, followlinks=False)
              # No follow link: to avoid recursive symlinks
              for fn in filenames
              if fn.endswith('.json')
        ):
            if os.path.islink(path):
                continue
            rel_path = os.path.relpath(path, zip_or_folder_input)
            with open(path, encoding='utf8') as f:
                data_input[rel_path] = json.load(f)
    else:
        logging.error('Bad file type: %s', zip_or_folder_input)
        return False
    
    analysis = analyze_data(data_input)
    with open(analysis_output, 'w', encoding='utf8') as f:
        json.dump(analysis, f, indent=2)
    return True

def _main():
    parser = argparse.ArgumentParser(description='Analyze Telemetry Data')
    parser.add_argument('--from', type=str, help='start date (YYYY/MM/DD)')
    parser.add_argument('--to', type=str, help='end date (YYYY/MM/DD)')
    parser.add_argument('-d', '--data-output', type=str, help='path of data output')
    parser.add_argument('-i', '--external-data', type=str, help='zip file or folder to external data input. This skips data downloading.')
    parser.add_argument('-a', '--analysis-output', type=str, required=True, help='path of analysis output')
    parser.add_argument('--log-level', type=str, help='log level (INFO, WARNING, ERROR)')
    parser.add_argument('-w', '--max-workers', type=int, default=50, help='Max workers (thread) count when fetching files from internet.')

    args = parser.parse_args()

    if not all((ACCESS_KEY_ID, ACCESS_KEY_SECRET, BUCKET_REGION, BUCKET_NAME)):
        print('Please configure bucket credentials in advance')
        sys.exit(1)
    
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s/%(name)s] %(message)s')
    
    log_level_map = {'INFO': logging.INFO, 'WARNING': logging.WARNING, 'ERROR': logging.ERROR}
    log_level_number: int | None = log_level_map.get(args.log_level)
    if args.log_level is not None:
        # logging.basicConfig(level=log_level_number)
        logging.getLogger().setLevel(log_level_number)
    
    if args.external_data:
        if not main_analyze_only(args.external_data, args.analysis_output):
            sys.exit(-1)
        return
    elif not args.data_output:
        print('Please specify --data-output')
        sys.exit(1)
    
    if getattr(args, 'from') and args.to:
        start_date_input = getattr(args, 'from')
        end_date_input = args.to
    else:
        # Default to yesterday
        yesterday = (datetime.now(tz=_timezone.utc) - timedelta(days=1)).strftime("%Y/%m/%d")
        start_date_input = yesterday
        end_date_input = yesterday
        print(f"Date unspecified, defaulted to yesterday: {yesterday}")
    
    main(start_date_input, end_date_input, args.data_output, args.analysis_output, args.max_workers)

if __name__ == '__main__':
    _main()
    