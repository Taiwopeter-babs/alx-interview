#!/usr/bin/python3
"""Implementing the lockbox algorithm"""


def canUnlockAll(boxes: list) -> bool:
    """
    Checks if all boxes can be unlocked.
    The function checks each box (list), and assigns a
    value of `True` to each key (number) found in it.

    Each key can unlock another box, so if at the end of the iteration
    a box is not found to be in the dictionary, then the function returns
    False.

    Args:
      boxes(list) - list of lists

    Returns:
        if each box (list) in the can be opened, the function
        returns True, otherwise False.

    """
    box_dict = {}
    box_len = len(boxes)
    i = 0

    if (len(boxes) == 0):
        return True

    # set the first box to True; it's already open
    box_dict[i] = True

    while i < box_len:
        # check if the key to the box is set to True
        if box_dict.get(i) is True:
            # set each key in the box to True
            for key in boxes[i]:
                box_dict[key] = True
                for k in boxes[key]:
                    box_dict[k] = True

        i += 1

    # check for all the available keys of the boxes
    for num in range(0, box_len):
        if box_dict.get(num) and box_dict.get(num) is True:
            continue
        else:
            return False
    return True
