# exercise 3, chapter 9. 01/01/2020 by SaidakbarP
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
    return winsA, winsB

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not (gameOver(scoreA, scoreB) or scoreA>15 or scoreB>15):
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
        #print(scoreA, scoreB)
    return scoreA, scoreB

def gameOver(a, b):
    return (a==15 and abs(a-b)>=2) or (b==15 and abs(b-a)>=2)


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Simulated games: ", n)
    print("Wins for A: {} {:0.1%}".format(winsA, winsA/n))
    print("Wins for B: {} {:0.1%}".format(winsB, winsB/n))

def main():
    printIntro()
    probA, probB, n = getInputs()
    #print(simOneGame(0.6,0.65))
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    main()
