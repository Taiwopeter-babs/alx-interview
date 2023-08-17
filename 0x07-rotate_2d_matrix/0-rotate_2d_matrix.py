#!/usr/bin/python3
"""
rotate 2d matrix
"""


def rotate_2d_matrix(matrix: list) -> None:
    """
    Rotates a 2d matrix
    """
    size = len(matrix)
    layer_count = size // 2

    # go through layers
    for layer in range(layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last - offset]
            left_side = matrix[last - offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last - offset] = right_side
            matrix[last - offset][first] = bottom
