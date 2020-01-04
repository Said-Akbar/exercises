# exercise 2, chapter 9. 01/01/2020 by SaidakbarP
# recquetball
from random import random

def printIntro():
    print("Racquetball game")

def getInputs():
    a = float(input("Enter the prob of A player winning when serving: "))
    b = float(input("Enter the prob of B player winning when serving: "))
    n = int(input("Enter the number of simulations: "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    shout = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA>scoreB:
            winsA += 1
        else:
            winsB += 1
        if shoutout(scoreA, scoreB):
            shout += 1
    return winsA, winsB, shout

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        #print(random())
        if shoutout(scoreA, scoreB):
            break
        if serving == "A": # when A is serving
            if random() < probA: # by random chance if randomness is smaller than the winning probability of A then A wins
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    return a==15 or b==15

def shoutout(a, b):
    return (a==7 and b==0) or (b==7 and a==0)

def printSummary(winsA, winsB, shout):
    n = winsA + winsB
    print("Simulated games: ", n)
    print("Wins for A: {} {:0.1%}".format(winsA, winsA/n))
    print("Wins for B: {} {:0.1%}".format(winsB, winsB/n))
    print("Shoutouts: {} {:0.1%}".format(shout, shout/n))

def main():
    printIntro()
    probA, probB, n = getInputs()
    #print(probA, probB, n)
    winsA, winsB, shout = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shout)

if __name__ == '__main__':
    main()
