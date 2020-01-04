# exercise 12 from chapter 9. 01/04/2020 by SaidakbarP
# random walk
from random import random

def coinflip():
    x = random()
    if x<.5:
        return -1
    elif x>=.5:
        return 1


def main():
    n = int(input("Enter number of steps: "))
    step = 0
    for i in range(n):
        result = coinflip()
        step += result
    print("The steps you have taken with random walk: ", step)
    print("average steps: ", abs(step)/n)


if __name__ == '__main__':
    main()
