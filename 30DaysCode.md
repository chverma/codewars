# Problem: Nested List Weight Sum II

## Statement

Given a nested list of integers `nested_list`, where each element can either be an integer or a list (which can contain integers or more lists), return the **sum of each integer in `nested_list` multiplied by its weight**.

The **weight** of an integer is calculated as:

> **weight = max_depth - depth + 1**

Where:

- **depth** is the number of nested lists an integer is contained within.
- **max_depth** represents the maximum depth of any integer in the `nested_list`.

---

## Constraints

- `1 ≤ nested_list.length ≤ 50`
- The integer values are in the range `[-100, 100]`
- `max_depth ≤ 50`

---

## Interface

```python

"""
This interface facilitates the creation of nested lists.
Do not implement or make assumptions about its implementation.
"""

class NestedInteger(object):
    def __init__(self, value=None):
        """
        If no value is specified, initializes an empty list.
        Otherwise, initializes with a single integer equal to the specified value.
        """

    def is_integer(self):
        """
        @return True if this NestedInteger holds a single integer rather than a nested list
        :rtype: bool
        """

    def add(self, elem):
        """
        Sets this NestedInteger to hold a nested list and adds the nested integer elem to it
        :rtype: void
        """

    def set_integer(self, value):
        """
        Sets this NestedInteger to hold a single integer equal to value
        :rtype: void
        """

    def get_integer(self):
        """
        @return the single integer this NestedInteger holds, if it holds a single integer
        Otherwise, return None if this NestedInteger holds a nested list
        :rtype: int
        """

    def get_list(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Otherwise, return None if this NestedInteger holds a single integer
        :rtype: List[NestedInteger]
        """
"""
:type nested_list: List[NestedInteger]
:rtype: int
"""
def weighted_depth_sum(nested_list):

    # Replace this placeholder return statement with your code
    return -1
