"""
 With this mission I want to start a series of missions with light bulbs. They will help you understand the concept of
 processes and evaluation of the processes’ performance. Instead of light bulbs, in real life, there may be equipment,
 the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated.

The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which the
light bulb switches its state. This means that if the light bulb is off and the button is pressed, the light turns on,
and if you press it again, it turns off.

The function input is an array of datetime objects - this is the date and time of pressing the button.
Your task is to determine how long the light bulb has been turned on.
"""

from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    count = len(els) - 1
    sec = 0
    while count > 0:

        res = els[count] - els[count-1]
        sec += res.total_seconds()
        count -= 2
    return int(sec)

if __name__ == '__main__':
    print("Example:")
    print(sum_light(els=[
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]))

    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]))