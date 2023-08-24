#!/usr/bin/python3
"""
Making change algorithm
"""


def makeChange(coins, total):
    """
    returns the fewest number of coins needed to meet
    a given value of `total`
    """
    remainder = total
    coin_count = 0
    list_size = len(coins)
    list_track = 0
    coin_index = 0
    # sort the list in reverse - make change from largest denomination
    sorted_coin_list = sorted(coins, reverse=True)

    if total <= 0:
        return 0

    while remainder > 0:
        # if end of the list is reached, coins options are exhausted
        if list_track == list_size:
            return -1
        # skip the coin denomination if difference will not give +ve value
        if remainder - sorted_coin_list[coin_index] < 0:
            coin_index += 1
            list_track += 1
            continue
        remainder -= sorted_coin_list[coin_index]

        coin_count += 1

    return coin_count
