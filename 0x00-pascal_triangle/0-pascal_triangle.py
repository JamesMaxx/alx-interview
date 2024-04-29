"""
Module documentation: Generate Pascal's triangle up to the nth row.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be 1 or greater.")

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
