#!/usr/bin/python3
""" Solves the pascal triangle problem """


def pascal_triangle(n):
    """ pascal triangle """
    row = 0
    pascal_coeff = 0
    pascal_list = []
    in_array = []

    if n <= 0:
        return []

    while row < n:
        col = 0

        while col <= row:
            if row == 0 or col == 0:
                pascal_coeff = 1
            else:
                pascal_coeff *= (row - col + 1) / col

            in_array.append(int(round(pascal_coeff, 1)))
            col += 1
        pascal_list.append(in_array)
        row += 1
        in_array = []

    return pascal_list
