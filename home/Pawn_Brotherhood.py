"""
 A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy,
 one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white
 pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.

Precondition:
0 < pawns ≤ 8
"""
def safe_pawns(pawns: set) -> int:
    pawns_index = set()
    for i in pawns:
        col = ord(i[0]) - 97
        row = int(i[1]) - 1
        pawns_index.add((col, row))

    count = 0

    for item in pawns_index:
        if (item[0]-1, item[1] - 1) in pawns_index :
            count += 1
        elif (item[0] + 1, item[1] - 1) in pawns_index:
            count += 1

    return count
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})) #6
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})) #1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")