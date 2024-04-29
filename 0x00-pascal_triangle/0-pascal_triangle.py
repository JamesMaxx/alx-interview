def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start a new row with 1
        for j in range(1, i):  # Calculate the elements in the new row
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle

# Test the function with n = 5
triangle = pascal_triangle(5)
for row in triangle:
    print(row)
