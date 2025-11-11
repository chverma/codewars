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
```

# 🧩 Problem Statement: Where Will the Ball Fall

You have **n** balls and a 2D grid of size **m × n** representing a box.
The box is open on the **top** and **bottom** sides. Each cell in the box has a diagonal that can redirect a ball to the **right** or **left**.

You must drop **n** balls — one from the top of each column.
The goal is to determine whether each ball will fall out of the bottom or become stuck in the box.

Each cell in the grid has a value of **1** or **−1**:

- **1** → the grid redirects the ball to the **right**.
- **−1** → the grid redirects the ball to the **left**.

A ball **gets stuck** if:
- It hits a **V-shaped** pattern between two diagonals (`1` next to `-1` forming a trap), or
- A diagonal redirects the ball into the **wall** of the box.

The solution should return an array of size **n**, where the *i-th* element is:
- the column number where the ball falls out at the bottom, or
- **−1** if the ball gets stuck.

If the ball drops from column **x** and falls out from column **y**,
then in the result array, `result[x] = y`.

---

## ⚙️ Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 ≤ m, n ≤ 100`
- `grid[i][j]` is `1` or `−1`

---

## 🧠 Example 1

**Input:**
```python
grid = [
  [1, 1, 1, -1, -1],
  [1, 1, 1, -1, -1],
  [-1, -1, -1, 1, 1],
  [1, 1, 1, 1, -1],
  [-1, -1, -1, -1, -1]
]
````

**Output:**

```python
[1, -1, -1, -1, -1]
```

**Explanation:**

* Ball from column `0` → falls out at column `1`.
* Balls from columns `1, 2, 3, 4` → get stuck.

---

## 🧩 Example 2

**Input:**

```python
grid = [
  [-1]
]
```

**Output:**

```python
[-1]
```

**Explanation:**
The ball hits the left wall and gets stuck.

---

## 🧩 Example 3

**Input:**

```python
grid = [
  [1, 1, 1, 1, 1, 1],
  [-1, -1, -1, -1, -1, -1]
]
```

**Output:**

```python
[0, 1, 2, 3, 4, -1]
```

**Explanation:**
All balls except the last one fall straight down; the last one gets stuck at the right wall.
