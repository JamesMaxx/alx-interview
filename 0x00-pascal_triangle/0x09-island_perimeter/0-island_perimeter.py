def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of integers): 2D grid where 0 represents water, 
                                         1 represents land.
    
    Returns:
        int: perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += _count_perimeter(grid, row, col)
    return perimeter


def _count_perimeter(grid, row, col):
    """
    Counts the perimeter of an island.
    
    Args:
        grid (list of list of integers): 2D grid where 0 represents water, 
                                         1 represents land.
        row (int): row index of the island.
        col (int): column index of the island.
    
    Returns:
        int: perimeter of the island.
    """
    perimeter = 4
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dr, dc in directions:
        if (row + dr >= 0 and row + dr < len(grid)
            and col + dc >= 0 and col + dc < len(grid[0])
            and grid[row + dr][col + dc] == 0):
            perimeter -= 1
    return perimeter
