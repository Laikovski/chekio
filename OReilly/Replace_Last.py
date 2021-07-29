"""
In a given list the last element should become the first one. An empty list or list with only one element should stay the same
"""

def replace_last(line: list) -> list:
    # your code here

    return [line.pop()] + line


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))