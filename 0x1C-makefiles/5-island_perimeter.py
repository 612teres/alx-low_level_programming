#!/usr/bin/python3

""" returns the perimeter of the island described in grid"""

def island_perimeter(grid):
    """This function returns the perimeter of an island.
       - Grid cells are connected horizontally/vertically (not diagonally).
        - Grid is rectangular, with width and height not exceeding 100.
        - Grid is completely surrounded by water, and there is one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island)
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
    return perimeter
