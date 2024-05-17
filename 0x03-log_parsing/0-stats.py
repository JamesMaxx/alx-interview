#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """
    Prints the current statistics of file size and status code counts.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    """
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final statistics after reading all lines
print_stats()
