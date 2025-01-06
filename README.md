# Python Average Calculation Bug

This repository demonstrates a potential bug in a Python function designed to calculate the average of a list of numbers. The function correctly handles empty lists, but fails to explicitly handle a list containing only zeros, leading to a division by zero error.

## Bug Description

The `calculate_average` function does not check for the case where all numbers in the input list are zero, resulting in a `ZeroDivisionError` when the list contains only zeros.

## Bug Solution

The solution involves adding a check to determine if the sum of the numbers is zero. If it is, then the average is zero; otherwise, the average is calculated as usual.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py`.
3. Observe the `ZeroDivisionError` when the input list contains only zeros.