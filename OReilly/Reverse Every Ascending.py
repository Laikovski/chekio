'''
Create and return a new iterable that contains the same elements as the argument iterable items, but with the
reversed order of the elements inside every maximal strictly ascending sublist. This function should not modify the
contents of the original iterable.
'''


def reverse_ascending(items):
    if not items:
        return
    sublist = [items[0]]
    for i in range(1, len(items)):
        if sublist[-1] < items[i]:
            sublist.append(items[i])
        else:
            yield from reversed(sublist)
            sublist = [items[i]]
    yield from reversed(sublist)



if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))