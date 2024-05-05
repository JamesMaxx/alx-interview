# Lockboxes

## Description

This Python script contains a method `canUnlockAll` that determines if all boxes in a list of lists can be opened based on the keys contained within them.

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS (or compatible environment)

## Usage

1. Ensure that Python 3.4.3 or a compatible version is installed on your system.
2. Save the provided `lockboxes.py` file to your local directory.
3. Open a terminal and navigate to the directory containing `lockboxes.py`.
4. Run the script using the command `python3 lockboxes.py`.

## Method Details

### canUnlockAll(boxes)

- **Description**: Checks if all boxes can be opened.
- **Arguments**:
  - `boxes`: A list of lists where each inner list represents a box and contains keys to other boxes.
- **Returns**:
  - `True` if all boxes can be opened, `False` otherwise.

## Test Cases

The script includes test cases to validate the functionality of the `canUnlockAll` method. These test cases are executed when the script is run directly.

## File Structure

- `lockboxes.py`: Contains the `canUnlockAll` method implementation and test cases.
- `README.md`: This file providing instructions and information about the script.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
