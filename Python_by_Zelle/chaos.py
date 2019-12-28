def main():
    print("Illustration of a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    y = eval(input("Enter the second number between 0 and 1:"))
    print("input {:.3f} {:.3f}".format(x,y))
    print("---------------------")
    for i in range(20):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print("{:.6f}    {:.6f}".format(round(x,6), round(y,6)))
main()
