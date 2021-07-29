"""
We have a List of booleans. Let's check if the majority of elements are true
"""

def is_majority(items: list) -> bool:
    # your code here
    if items.count(True) > len(items) // 2:
        return True
    elif len(items) == 1 and items[0] == True:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))
    print(is_majority([True, True, False, False]))
    print(is_majority([]))
    print(is_majority([False]))