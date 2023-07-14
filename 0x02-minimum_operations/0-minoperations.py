#!/usr/bin/python3
"""Minimum operations algorithm"""
from typing import Dict


def minOperations(n: int) -> int:
    """
    returns the minimum number of operations
    that will give exactly n number of characters
    """
    if n is None or n <= 0 or not isinstance(n, int):
        return 0

    # set copy and paste keys
    allowed_keys = {'C-A': 0, 'C-V': 0}

    key_count = 0
    h_count = 1  # number of characters currently in print
    h_chars_in_buffer = 0  # 'H' chars stored when 'copy' key is used

    while h_count < n:
        if n % h_count == 0:
            # increase count of keys used and double 'H' chars
            allowed_keys['C-A'] += 1
            allowed_keys['C-V'] += 1
            key_count += 2
            h_chars_in_buffer = h_count
            h_count *= 2

        else:
            # increase only count of 'paste' key
            allowed_keys['C-V'] += 1
            # increase key count by 1
            key_count += 1
            # 'H' chars is doubled by the current number of chars in buffer
            h_count = h_chars_in_buffer + h_count
            # print('number of H characters === {}\t key_count = [{}]'.format(
            #     h_count, key_count))
    return key_count
