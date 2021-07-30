"""
 This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.

You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit.
Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only
to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program
for the entire period.
"""
from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None):
    count_1 = 0
    if start_watching != None:

        for i in range(len(els)-1):

            if start_watching >= els[i] and start_watching <= els[i + 1]:

                els[i] = start_watching
                count_1 = i
                break

    els = els[count_1:]

    count = len(els) - 1
    sec = 0
    while count > 0:

        res = els[count] - els[count-1]
        sec += res.total_seconds()
        count -= 2
    return int(sec)


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )
    print(sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        ))
    print(sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        ))
    print(sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        ))

    print(sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        ))