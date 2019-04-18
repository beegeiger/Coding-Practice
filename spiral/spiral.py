"""Print points in matrix, going in a spiral.

Give a square matrix, like this 4 x 4 matrix, it's composed
of points that are x, y points (top-left is 0, 0):

    0,0  1,0  2,0  3,0
    0,1  1,1  2,1  3,1
    0,2  1,2  2,2  3,2
    0,3  1,3  2,3  3,3

Starting at the top left, print the x and y coordinates of each
point, continuing in a spiral.

(Since we provide 3 different versions, you can change this to
the routine you want to test:

    >>> spiral = spiral_by_nested_boxes

Here are different sizes:

    >>> spiral(1)
    (0, 0)

    >>> spiral(2)
    (0, 0)
    (1, 0)
    (1, 1)
    (0, 1)

    >>> spiral(3)
    (0, 0)
    (1, 0)
    (2, 0)
    (2, 1)
    (2, 2)
    (1, 2)
    (0, 2)
    (0, 1)
    (1, 1)

    >>> spiral(4)
    (0, 0)
    (1, 0)
    (2, 0)
    (3, 0)
    (3, 1)
    (3, 2)
    (3, 3)
    (2, 3)
    (1, 3)
    (0, 3)
    (0, 2)
    (0, 1)
    (1, 1)
    (2, 1)
    (2, 2)
    (1, 2)
"""

# class Grid(object):
#     def __init__(self):
#         self._grid = []
#         self.head = None

#     def push(self, item):
#         """Add item to top."""

#         self._stack.append(item)

#     def pop(self):
#         """Remove top item."""

#         return self._stack.pop()

#     def peek(self):
#         """Return, but don't remove, top item."""

#         return self._stack[-1]

#     def is_empty(self):
#         """Is the stack empty?"""

#         return not self._stack

# class Node(object):
#     """Node in a linked list."""

#     def __init__(self, data):
#         self.data = data
#         self.next = None


def spiral_by_nested_boxes(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size."""

    for box_num in range(0, matrix_size // 2):
        top = left = box_num
        bottom = right = matrix_size - box_num - 1
        for x in range(left,right):
            print((x, top))
        for y in range(top,bottom):
            print((right, y))
        for x in range(right, left, -1):
            print((x, bottom))
        for y in range(bottom, top, -1):
            print((left, y))
    
    if matrix_size % 2 != 0:
        print((matrix_size // 2, matrix_size // 2))



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n")
