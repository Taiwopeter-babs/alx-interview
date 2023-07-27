#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data: list) -> bool:
    """
    Validates the dataset represented by a set of integers
    are valid utf-8 encoding
    """
    if len(data) == 0 or not isinstance(data, list):
        return False

    continuation_bytes = 0
    for num in data:
        # print(num, bin(num))
        if continuation_bytes == 0:
            # binary equivalent of 110xxxxx is 5
            if num >> 5 == 0b110:
                continuation_bytes = 1
            # binary equivalent of 1110xxxx is 14
            elif num >> 4 == 0b1110:
                continuation_bytes = 2
            # binary equivalent of 11110xxx is 30
            elif num >> 3 == 0b11110:
                continuation_bytes = 3
            elif num >> 7 != 0:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            continuation_bytes -= 1
    return True
