#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    island perimeter algorithm
    """
    size_portion = len(grid[0])
    hor = 0
    ver = 0
    perimeter = island_recurse(grid, ver, hor, size_portion)

    # add 1 to account for the starting point
    return 2 * (perimeter + 1)

def island_recurse(grid, ver, hor, size_portion):
    """
    helper function
    """
    width = 0
    height = 0
    
    if hor == size_portion or ver == len(grid):
        return 0

    if grid[ver][hor] == 0:
      if hor == size_portion - 1:
         return island_recurse(grid, ver + 1, 0, size_portion)
      return island_recurse(grid, ver, hor + 1, size_portion)
    
    
    # check if vertical land continues
    if grid[ver + 1][hor] == 1:
      height = island_recurse(grid, ver + 1, hor, size_portion)
      # print('height', height)

    # check if horizontal land continues
    if grid[ver][hor + 1] == 1:
      #  print('hor', hor)
        width = island_recurse(grid, ver, hor + 1, size_portion)
        # print('width', width)
    
    return height + width + 1      
