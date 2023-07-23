#!/usr/bin/python3
"""
Reads data from stdin line by line parses it, and prints
it. After every 10 lines or KeyBoardInterrupt Error, the statistics
will be printed from beginning.

"""
import re
from sys import stdin


def parse_log_data():
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
        r'[0-9.\w]+\s*\-\s*\[[0-9-\s+:.]+\]\s\"GET')

    match_two = re.compile(
        r'\s\/projects\/260\sHTTP\/1\.1\"\s\d{3}\s[0-9]+$'
    )

    count = 0
    total_size = 0

    try:
        for line in stdin:
            # skip line if no adherence to format
            if not match_one.search(line) or not match_two.search(line):
                continue
            code, file_size = line.rsplit(" ", 2)[1:]
            status_codes[code] += 1
            total_size += int(file_size)
            # show data at tenth count
            if count == 9:
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
                # reset the count
                count = 0
                continue  # continue to the next line

            count += 1  # increment count to begin the new line

    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))


if __name__ == '__main__':
    parse_log_data()
