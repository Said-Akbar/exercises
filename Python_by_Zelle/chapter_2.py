# checking if the loop is going to execute print. It should not!
print("start")
for i in range(0):
    print("Hello")
print("end")

# exercise 1
def main():
    print("This program converts celcius to fahrenheit")
    celsius = eval(input("Please, enter the temperature in C: "))
    fahrenheit = 9/5*celsius + 32
    print("The temperature in F: ", fahrenheit)
    #input("Press enter to exit")

    print()
    print("Finding average of 3 numbers")
    score1, score2, score3 = eval(input("Enter 3 numbers seperated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of three numbers is: ", average)

    print()
    print("This program generates a table of celcius to fahrenheit conversion")
    for i in range(0, 101, 10):
        fahrenheit = 9/5*i + 32
        print("The temperature in C {} degrees corresponds to F {} degrees".format(i, fahrenheit))
    input("Press enter to exit")

    print()
    print("Future values of your investments")
    initial = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the years to invest: "))
    principal = initial
    for i in range(year):
        principal = principal*(1+apr)
        principal = principal + initial
    print("Total value in ", year, "is: ", principal)

    print()
    print("Simple calculator. To quit type a letter")
    for i in range(100):
        calc = eval(input("Enter the expression:"))
        print("The answer is: ", calc)

main()
