ft_package

A simple Python package with useful utility functions.

Build:
run in the terminal inside the ft_package main directory: pip install build twine
run in the terminal inside the ft_package main directory: python3 -m build
run in the terminal inside the ft_package main directory: twine upload dist/* and enter this api key : pypi-AgEIcHlwaS5vcmcCJGRmNDVjZmZkLWFjMGQtNDBmZi1iN2Y3LTM3MmMzZTUwOTZmYgACKlszLCJkNGQwODA1NS01ZGUwLTQyYmYtOWE3MS1jNTVmZmEwMjEyY2MiXQAABiAHbFCUDfVctBnYSLEti0nddRjhEx7XIQmFmqgwum9MaA


Installation:
pip install ft-package

Usage:
from ft_package import count_in_list, unique_elements, flatten_list, reverse_string

print(count_in_list(["apple", "banana", "apple"], "apple")) # Output: 2
print(unique_elements([1, 2, 2, 3, 4])) # Output: [1, 2, 3, 4]
print(flatten_list([[1, 2], [3, 4], [5]])) # Output: [1, 2, 3, 4, 5]
print(reverse_string("hello")) # Output: "olleh"
