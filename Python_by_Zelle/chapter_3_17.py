# Chapter 3 ex 17. 12/28/2019 by Saidakbarp
# computing the square root by Newton's method
import math
def main():
    x = int(input("Enter the number you want the square root of: "))
    n = int(input("Enter the iterations to improve accuracy: "))
    root = x/2
    for i in range(n):
        root = (root+x/root)/2 # update root each iteration
        print("difference from the real root: ", round(math.sqrt(x),2),"-",
        round(root,2), " = ", round(round(math.sqrt(x),2)-round(root,2),2))

main()
