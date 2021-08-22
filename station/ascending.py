"""
 Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger
 than (and not merely equal to) the preceding element.

Input: Iterable with ints.

Output: Bool.
"""


def is_ascending(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i+1]:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    print(is_ascending([4, 5, 6, 7, 3, 7, 9]))
    print(is_ascending([]))