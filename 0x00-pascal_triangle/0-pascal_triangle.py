#!/usr/bin/python3
"""
Returns a list of lists representing the first n rows of Pascal's triangle.

Args:
    n (int): The number of rows of Pascal's triangle to return.

Returns:
    list: A list of lists representing the first n rows of Pascal's triangle.
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]  # first row of Pascal's triangle
    for i in range(1, n):
        """
        Calculate the i-th row of Pascal's triangle.

        i: row number (0-indexed)
        """
        row = [1]  # first element of i-th row
        for j in range(1, i):
            """
            Calculate the j-th element of the i-th row of Pascal's triangle.

            j: element number (0-indexed)
            """
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # last element of i-th row
        triangle.append(row)
    return triangle

