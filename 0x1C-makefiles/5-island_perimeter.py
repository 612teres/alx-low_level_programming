#!/usr/bin/python3
""" Returns the perimeter of a island """


def island_perimeter(grid):
    """ Each cell contains either 0 for water or 1 for land.
        Grid cells are connected horizontally/vertically
        The grid is rectangular and does not exceed 100 in width or height.
        The grid is completely surrounded by water, and there is one island or nothing.
        The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island)
    """
perimeter = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
return (perimeter)
