# ex14 chapter 6 12/28/2019 SaidakbarP
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
def sumList(nums):
    x = 0
    for i in nums:
        x = x + i
    return x
def toNumbers(strList):
    #print(strList)
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def main():
    test = open("sum.txt", "w")
    for line in range(1):
        x = list(range(1,11))
        print(x, file=test, end="\n")
    test.close()
    infile = input("Enter the file name in current folder:")
    infile = open(infile, "r")
    numz = []
    for line in infile:
        numz = line[1:-2]
        numz = numz.split(',')
        toNumbers(numz)
        squareEach(numz)

    print(sumList(numz))

if __name__== "__main__":
    main()
