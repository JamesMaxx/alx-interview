# 0. Rotate 2D Matrix

## Project Overview

In this project, you are tasked with implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python.

## Key Concepts

### Matrix Representation in Python

- **Understanding 2D Matrices**: In Python, 2D matrices are represented using lists of lists. Each element in the main list is a row of the matrix.
- **Accessing and Modifying Elements**: You can access and modify elements in a 2D matrix using indices, e.g., `matrix[i][j]` for the element in the `i-th` row and `j-th` column.

### In-place Operations

- **Definition**: Performing operations on data without creating a copy of the data structure.
- **Importance**: Minimizing space complexity by modifying the matrix in place is crucial for optimizing performance.

### Matrix Transposition

- **Concept**: Transposing a matrix involves swapping rows and columns, i.e., converting the `i-th` row into the `i-th` column.
- **Implementation**: This is typically the first step in rotating the matrix.

### Reversing Rows in a Matrix

- **Manipulation**: After transposing the matrix, each row needs to be reversed to achieve the 90-degree clockwise rotation.

### Nested Loops

- **Usage**: Nested loops are essential for iterating through 2D data structures like matrices.
- **Modification**: Use nested loops to modify elements within the matrix to achieve the desired rotation.

## Resources

### Python Official Documentation

- **Data Structures**: Learn about list comprehensions and nested list comprehensions.
  - [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles

- **Inplace Rotate Square Matrix by 90 Degrees**: A detailed article on how to rotate a matrix in place.
  - [Inplace Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **Transpose a Matrix in Single Line in Python**: Learn to transpose a matrix efficiently.
  - [Transpose a Matrix in Single Line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint

- **Python Lists**: Basics of list manipulation in Python.
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Approach

1. **Transpose the Matrix**: Convert rows into columns.
2. **Reverse Each Row**: Reverse the order of elements in each row.

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically. First, transpose the matrix and then reverse each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving your problem-solving and algorithmic thinking skills in Python.

## Example

Given the following matrix:
