#!/usr/bin/python3

import re
import sys


def extract_input(input_line):
    pattern = (
        r'\s*(?P<ip>\S+)\s*'
        r'\-\s*\[\s*(?P<date>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d+)\]\s*'
        r'"GET\s+/\S+\s+HTTP/\d+\.\d+"\s*'
        r'(?P<status_code>\d+)\s*'
        r'(?P<file_size>\d+)'
    )
    match = re.fullmatch(pattern, input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return None


def print_statistics(total_file_size, status_codes_stats):
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print(f'{status_code}: {num}')


def update_metrics(line, total_file_size, status_codes_stats):
    line_info = extract_input(line)
    if line_info:
        status_code = line_info['status_code']
        file_size = line_info['file_size']
        total_file_size += file_size
        status_codes_stats[status_code] = status_codes_stats.get(status_code, 0) + 1
    return total_file_size


def run():
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin:
            line_num += 1
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

