import logging
import json
from .bucket_spec import RemoteBucket
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone as _timezone, timedelta
from typing import Iterable, Optional


def parse_iso_time(time_str: str) -> Optional[datetime]:
    if not time_str:
        return None
    try:
        time_str = time_str.replace('Z', '+00:00')
        dt = datetime.fromisoformat(time_str)
        return dt
    except Exception:
        return None

def date_range(start_date_str: str, end_date_str: str) -> list[str]:
    start = datetime.strptime(start_date_str, "%Y/%m/%d")
    end = datetime.strptime(end_date_str, "%Y/%m/%d")
    
    if start > end:
        raise ValueError('start > end')

    current = start
    dates = []
    while current <= end:
        dates.append(current.strftime("%Y/%m/%d"))
        current += timedelta(days=1)
    return dates

def sort_dict_by_value(d: dict) -> dict:
    sorted_items = sorted(d.items(), reverse=True, key=lambda x: x[1])
    return dict(sorted_items)

def fetch_files(date_prefixes: Iterable[str], remote_bucket: RemoteBucket, max_workers: int = 10) -> Iterable[dict]:
    def _fetch_and_parse_single_file(key):
        try:
            content = b''.join(remote_bucket.get_file_content(key))
            content_as_json = json.loads(content)
            assert isinstance(content_as_json, dict), 'Not a JSON object'
            return {'status': 'success', 'key': key, 'data': content_as_json}
        except Exception as e:
            return {'status': 'fail', 'key': key, 'error': str(e)}

    keys_to_fetch = []
    for date_prefix in date_prefixes:
        logging.info(f'Scanning date: {date_prefix}')
        keys_to_fetch.extend(key for key in remote_bucket.list_files(prefix=date_prefix) if key.endswith('.json'))
    
    logging.info(f"Found {len(keys_to_fetch)} JSON files to fetch.")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_key = {executor.submit(_fetch_and_parse_single_file, key): key for key in keys_to_fetch}
        
        for future in as_completed(future_to_key):
            result = future.result()
            if result['status'] == 'success':
                logging.debug(f"Successfully fetched: {result['key']}")
            else:
                logging.warning(f"Failed to fetch {result['key']}: {result['error']}")
            yield result

def analyze_data(data_list: dict[str, dict]) -> dict:
    telemetry_level = defaultdict(int)
    mod_version = defaultdict(int)
    mod_platform = defaultdict(int)
    mc_version = defaultdict(int)
    country = defaultdict(int)
    timezone = defaultdict(int)
    geo_via_reverse_proxy = 0
    hooks_e_current = defaultdict(int)
    hooks_p_current = defaultdict(int)
    hooks_e_all = defaultdict(int)
    hooks_p_all = defaultdict(int)
    schema = defaultdict(int)
    # Hybrid statistics
    hyb_platform_mcv = defaultdict(int)
    hyb_mov_platform_mcv = defaultdict(int)

    for data in data_list.values():
        data_telemetry_level = data.get('telemetry_level', -1)
        if not isinstance(data_telemetry_level, int):
            logging.warning('Invalid data: %s. Skipping.', data)
            continue
        telemetry_level['lvl' + str(data_telemetry_level)] += 1

        if data_telemetry_level < 1:
            continue

        data_schema = data.get('schema')
        schema[data_schema] += 1

        data_mod_version = str(data.get('mod_version'))
        data_mc_version = str(data.get('mc_version'))
        data_mod_platform = str(data.get('mod_platform'))
        mod_version[data_mod_version] += 1
        mod_platform[data_mod_platform] += 1
        mc_version[data_mc_version] += 1
        hyb_platform_mcv[f'{data_mod_platform}-{data_mc_version}'] += 1
        hyb_mov_platform_mcv[f'{data_mod_version}@{data_mod_platform}-{data_mc_version}'] += 1

        data_client_context: dict = dict(data.get('client_context', {}))
        data_country = str(data_client_context.get('country', {}).get('code'))
        data_timezone = str(data_client_context.get('timezone'))
        proxy_context: dict = dict(data.get('proxy_context', {}))

        country[data_country] += 1
        timezone[data_timezone] += 1
        if proxy_context.get('via_reverse_proxy', False):
            geo_via_reverse_proxy += 1

        if data_schema < 2:
            continue

        data_current_hooks: dict[str, str] = dict(data.get('current_hooks', {}))
        data_current_hooks_e: str = str(data_current_hooks.get('enchantment'))
        data_current_hooks_p: str = str(data_current_hooks.get('potion'))

        if data_telemetry_level < 2:
            continue
        
        data_all_hooks: dict[str, list[str]] = dict(data.get('all_hooks'), {})
        data_all_hooks_e: tuple[str] = tuple(data_all_hooks.get('enchantment', ()))
        data_all_hooks_p: tuple[str] = tuple(data_all_hooks.get('potion', ()))
        hooks_e_current[data_current_hooks_e] += 1
        hooks_p_current[data_current_hooks_p] += 1
        for k in data_all_hooks_e: hooks_e_all[str(k)] += 1
        for k in data_all_hooks_p: hooks_p_all[str(k)] += 1

    ret = {
        'client_meta': {
            'telemetry_level': telemetry_level,
            'schema': schema,
            'mod': {
                'mod_version': sort_dict_by_value(mod_version),
                'mc_version': sort_dict_by_value(mc_version),
                'mod_platform': sort_dict_by_value(mod_platform),
                'hybrid': {
                    'platform_mcv': sort_dict_by_value(hyb_platform_mcv),
                    'mov_platform_mcv': sort_dict_by_value(hyb_mov_platform_mcv),
                },
            },
            'context': {
                'country': sort_dict_by_value(country),
                'timezone': sort_dict_by_value(timezone),
                'geo_via_reverse_proxy': geo_via_reverse_proxy,
            },
        },
        'customization': {
            'current_hooks': {
                'enchantment': sort_dict_by_value(hooks_e_current),
                'potion': sort_dict_by_value(hooks_p_current),
            },
            'all_hooks': {
                'enchantment': sort_dict_by_value(hooks_e_all),
                'potion': sort_dict_by_value(hooks_p_all)
            },
        },
        'generated_at': datetime.now(tz=_timezone.utc).isoformat()
    }

    return ret








