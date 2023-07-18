#!/usr/bin/python3
"""
Reads data from stdin line by line parses it, and prints
it. After every 10 lines or KeyBoardInterrupt Error, the statistics
will be printed from beginning.

"""
from sys import stdin
import re


def parse_log_data() -> None:
    """
    The stdin format:
    ### <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    ### <file size>

    The possible status codes are:
    ### 200, 301, 400, 401, 403, 404, and 500

    The printed output to stdout will show:
    #### File size: <total file size of previous ten lines>
    #### <status code>: <number of lines by status code>
    Example:
            File size: 2345
            200: 3
            301: 3
            400: 4
            401: 2
            403: 5
    """
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    # define matching formats for read input
    match_one = re.compile(
        r'[0-9.]+\s+\-\s+\[[0-9-\s+:.]+\]\s\"GET')

    match_two = re.compile(
        r'\s\/projects\/260\sHTTP\/1\.1\"\s\d{3}\s[0-9]+$'
    )

    count = 0
    total_size = 0
    while True:
        try:
            line = stdin.readline()
            if not line:
                break
            if not match_one.search(line) or not match_two.search(line):
                continue
            line = line.replace('\n', '')
            code, file_size = line.rsplit(" ", 2)[1:]
            status_codes[code] += 1
            total_size += int(file_size)

        except KeyboardInterrupt:
            print("File size: {}".format(total_size))
            for key in status_codes:
                if status_codes.get(key) != 0:
                    print("{}: {}".format(key, status_codes.get(key)))
            count = 0

        if count == 9:
            print("File size: {}".format(total_size))
            for key in status_codes:
                if status_codes.get(key) != 0:
                    print("{}: {}".format(key, status_codes.get(key)))
            count = 0
        else:
            count += 1


parse_log_data()
