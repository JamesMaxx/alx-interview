#!/usr/bin/python3
"""
Determines if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    Args:
    - boxes: A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
    - True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])  # Start with the key to the first box (box 0)
    visited = set()  # Set to track visited boxes

    while keys:
        current_box = keys.pop()  # Get a box with a key
        visited.add(current_box)  # Mark the box as visited

        # Add keys from the current box to the set of keys
        keys.update(boxes[current_box])

        # Check if all boxes have been visited
        if len(visited) == len(boxes):
            return True

    return False

# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
