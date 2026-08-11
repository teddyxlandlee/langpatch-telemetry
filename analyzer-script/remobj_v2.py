import argparse
import itertools
import logging
import math
import os
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable, Generator
from .bucket_spec import RemoteBucket, RemoteBucketConstructor

try:
    from dotenv import load_dotenv
except ImportError:
    if __name__ == '__main__':
        print('Error: dotenv not found. Please configure venv first.')
        sys.exit(-1)
    else:
        raise

# Load .env from internal_stats, expecting variable names with _DEL suffix.
# e.g. BUCKET_ACCESS_KEY_ID -> BUCKET_ACCESS_KEY_ID_DEL
load_dotenv(dotenv_path=os.path.join(os.path.dirname(sys.argv[0]), '..', 'internal_stats', '.env'))

DEL_ACCESS_KEY_ID = os.getenv('BUCKET_ACCESS_KEY_ID_DEL')
DEL_ACCESS_KEY_SECRET = os.getenv('BUCKET_ACCESS_KEY_SECRET_DEL')
DEL_BUCKET_NAME = os.getenv('BUCKET_NAME_DEL')
DEL_BUCKET_REGION = os.getenv('BUCKET_REGION_DEL')
# =============

logger = logging.getLogger('remobj_v2')

# Maximum keys per single delete_files call (imposed by bucket API)
_BATCH_SIZE = 1000


def connect_to_remote_storage(max_workers: int = 200) -> RemoteBucket:
    ctr: RemoteBucketConstructor
    provider = os.getenv('BUCKET_PROVIDER_DEL', '').lower()
    logger.info('Connecting to remote storage (provider: %s, region: %s, bucket: %s) ...',
                provider, DEL_BUCKET_REGION, DEL_BUCKET_NAME)
    match provider:
        case 'aliyun':
            from .bucket_aliyun import AliyunBucket
            ctr = AliyunBucket
        case 'tencent':
            from .bucket_tencent import TencentBucket
            ctr = TencentBucket
        case _:
            raise NotImplementedError('Unsupported bucket provider: ' + os.getenv('BUCKET_PROVIDER_DEL', '<unknown>'))
    logger.info('Initializing bucket client...')
    bucket = ctr(
        bucket_name=DEL_BUCKET_NAME,
        access_key_id=DEL_ACCESS_KEY_ID,
        access_key_secret=DEL_ACCESS_KEY_SECRET,
        region=DEL_BUCKET_REGION,
        max_workers=max_workers,
    )
    logger.info('Connected to remote storage successfully.')
    return bucket


def collect_keys_from_zip(zip_path: str) -> list[str]:
    """Collect all non-folder entries from a zip file and return their normalized paths."""
    with zipfile.ZipFile(zip_path, 'r') as zf:
        return [entry.filename for entry in zf.infolist() if not entry.is_dir()]


def _batched(iterable: Iterable, n: int) -> Generator:
    """Yield successive n-sized chunks from iterable."""
    itr = iter(iterable)
    while True:
        chunk = list(itertools.islice(itr, n))
        if not chunk:
            return
        yield chunk


def _delete_batch(bucket: RemoteBucket, keys: list[str]) -> tuple[int, list[str]]:
    """Delete a batch of keys (≤_BATCH_SIZE). Returns (success_count, error_messages)."""
    errors = list(bucket.delete_files(keys))
    succeeded = len(keys) - len(errors)
    return succeeded, errors


def main(zip_path: str, max_workers: int):
    remote_bucket = connect_to_remote_storage(max_workers=max_workers)

    logger.info('Collecting object keys from zip: %s', zip_path)
    keys_to_delete = collect_keys_from_zip(zip_path)

    if not keys_to_delete:
        logger.warning('No files found in the zip archive. Nothing to delete.')
        return

    logger.info('Collected %d object key(s) from zip.', len(keys_to_delete))

    # Split into batches of at most _BATCH_SIZE
    logger.info('Splitting keys into batches...')
    batches = _batched(keys_to_delete, _BATCH_SIZE)
    batches_len_estimated = math.ceil(len(keys_to_delete) / _BATCH_SIZE)
    logger.info('Split into %d batch(es) (max %d keys/batch).', batches_len_estimated, _BATCH_SIZE)

    logger.info('Submitting %d delete tasks (max_workers=%d)...', batches_len_estimated, max_workers)

    total_succeeded = 0
    total_failed = 0

    completed = 0
    last_logged_percent = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_batch = {
            executor.submit(_delete_batch, remote_bucket, batch): (i + 1, batch)
            for i, batch in enumerate(batches)
        }
        logger.info('All tasks submitted. Waiting for completion...')
        for future in as_completed(future_to_batch):
            batch_no, batch = future_to_batch[future]
            try:
                succeeded, errors = future.result()
                total_succeeded += succeeded
                total_failed += len(errors)
                if errors:
                    logger.warning(
                        'Batch %d: %d succeeded, %d failed. Sample: %s',
                        batch_no, succeeded, len(errors), errors[0],
                    )
                else:
                    logger.info('Batch %d: all %d succeeded.', batch_no, succeeded)
            except Exception as e:
                total_failed += len(batch)
                logger.error('Batch %d failed entirely: %s', batch_no, e)

            completed += 1
            current_percent = int(completed * 100 / batches_len_estimated)
            if current_percent > last_logged_percent:
                last_logged_percent = current_percent
                logger.info('Deleting remote objects... %s%%', current_percent)

    logger.info(
        'Done. Deleted %d object(s), encountered %d error(s).',
        total_succeeded, total_failed,
    )


def _main(raw_args: Iterable[str] | None = None):
    parser = argparse.ArgumentParser(description='Remove remote objects matching entries in a local zip archive.')
    parser.add_argument(
        '-f', '--list',
        type=str,
        required=True,
        help='Path to a zip file whose non-folder entries correspond to remote object keys to delete.',
    )
    parser.add_argument(
        '--log-level',
        type=str,
        default='INFO',
        help='Log level (DEBUG, INFO, WARNING, ERROR)',
    )
    parser.add_argument(
        '-w', '--max-workers',
        type=int,
        default=50,
        help='Max worker threads for concurrent deletion.',
    )

    args = parser.parse_args(raw_args)

    del_provider = os.getenv('BUCKET_PROVIDER_DEL', '').strip()
    if not all((DEL_ACCESS_KEY_ID, DEL_ACCESS_KEY_SECRET, DEL_BUCKET_REGION, DEL_BUCKET_NAME)) or not del_provider:
        print(
            'Please configure deletion credentials in advance.\n'
            'Expected env vars (with _DEL suffix):\n'
            '  BUCKET_ACCESS_KEY_ID_DEL\n'
            '  BUCKET_ACCESS_KEY_SECRET_DEL\n'
            '  BUCKET_NAME_DEL\n'
            '  BUCKET_REGION_DEL\n'
            '  BUCKET_PROVIDER_DEL'
        )
        sys.exit(1)
    
    log_levels = {'INFO': logging.INFO, 'DEBUG': logging.DEBUG, 'ERROR': logging.ERROR, 'WARNING': logging.WARNING}

    logging.basicConfig(
        level=log_levels.get(args.log_level),
        format='%(asctime)s [%(levelname)s/%(name)s] %(message)s',
    )

    if not zipfile.is_zipfile(args.list):
        print('Error: --list / -f must point to a valid zip file.')
        sys.exit(1)

    main(args.list, args.max_workers)


if __name__ == '__main__':
    _main()