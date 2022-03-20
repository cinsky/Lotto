# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import math
from time import sleep

allBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45]
s = 6 * math.pi * math.e / 45

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def run():
    t = 44
    l = []
    ball = allBall.copy()

    for i in range(1,7):
        sleep(s)
        b = random.randint(0, t)
        l.append(ball[b])
        #print(f'Count:{i}, Ball count:{len(ball)}, Ball Number:{ball[b]}')
        del ball[b]
        t -= 1

    l.sort()
    return l

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(f'Sleep time is {s}sec')

    a = []
    for x in range(1,46):
        a.append(0)

    for y in range(1,6):
        r = run()
        for z in range(len(r)):
            a[r[z]-1] += 1

        print(f'C:{y}, Ball:{r}')
        sleep(s*s)

    print(a)








