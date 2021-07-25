"""
 One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions
 on how to get around the ship. But this robot is left-handed and has a tendency to joke around and confuse its
 right-handed friends.

You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings
are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with
the word "left", even if it's a part of another word. All strings are given in lowercase.

Input: A sequence of strings.
Output: The text as a comma-separated string.
"""


def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    res = ''
    for i in phrases:

        if 'right' in i:
            res += i.replace('right', 'left') + ','
        else:
            res += i + ','
    return res.rstrip(',')

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    print(left_join(("enough", "jokes")))