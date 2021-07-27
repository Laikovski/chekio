"""
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the
non-unique elements in this list. To do so you will need to remove all unique elements
(elements which are contained in a given list only once). When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
"""




def checkio(data: list) -> int:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    new_arr = []
    for i in data:
        if data.count(i) != 1:
            new_arr.append(i)
    return new_arr

print(list(checkio([1, 2, 3, 4, 5])))
print(list(checkio([5, 5, 5, 5, 5])))
print(list(checkio([10, 9, 10, 10, 9, 8])))