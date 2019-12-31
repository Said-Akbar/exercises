# exercises from chapter 8. 12/29/2019 SaidakbarP
# discussion 3
def sum_n(n):
    x = 0
    counter = 1
    while counter<=n:
        x = x + counter
        counter += 1
    return x

def sum_odd(n):
    total = 0
    counter = 1 # 1 3 5 7 9 11...
    while counter<=n:
        total += counter
        counter += 2
    return total

def interactive_sum():
    total = 0
    x = int(input("Enter value (999 to quit): ")) # priming read for sentinel loop
    while x!=999:
        total += x
        x = int(input("Enter value (999 to quit): "))
    return total

def division_bytwo(n):
    counter = 0
    current = n
    while current>1:
        current //= 2
        counter += 1
    return counter
#ex 1
def fibonacci(n):
    total = 0
    prev = 1
    counter = 1
    while counter<=n:
        total += prev        # 1 1 2 3 ...
        prev = total - prev  # 0 1 1 2 ...
        counter += 1
    return total

#ex2
def wind_index(V, T):
    w_index = 35.74+0.6215*T - 35.75*V**(0.16) + 0.4275*T*V**(0.16)
    return w_index

def windchill():
    windspeed = 0
    while windspeed<=50:
        Temp = -20
        print("{:<2}".format(windspeed), end=" ")
        while Temp<=60:
            if windspeed == 0:
                print("{:>7}".format(Temp), end="")
            else:
                value = wind_index(windspeed, Temp)
                print("{:>7.2f}".format(value), end="")
            Temp += 10
        print()
        windspeed += 5
#ex3
def double_invest(usd, interest):
    years = 0
    total = usd
    while total <= (usd*2):
        total = total*(1+interest)
        years += 1
    return years
# ex 5 Check if the number is prime
def is_prime(n):
    # from 2 till n**(1/2) check if n is evenly divisible by i
    up_limit = int(n**(1/2))
    i = 3
    if n % 2 == 0: # we can skip two just checking once so that we avoid incrementing by 1
        return False # 2 is a special case, but we can actually create the list is each numbers multiples up to sqrt(n) to avoid extra calculations
    while i <= up_limit:
        if n % i == 0:
            return False
        i += 2
    return True

# ex 6 Print primes up to n
def print_prime(n):
    # iterate through i=2...n
    #   iterate through 3...i:
    counter = 2 # I know this algorithm is not effective, but will do for now.
    primes = []
    while counter<=n:
        if is_prime(counter):
            primes.append(counter)
        counter += 1
    return primes
# ex 7
def sum_primes_even(n):
    # we have to create a list of prime numbers up to n-2, then check combination of each two elements
    # e.g. 16. list of primes: 2, 3, 5, 7, 11, 13. start from 0th element. 2 and  take the largest= 13
    # 2+13 != 16. move to next element: 3+13 == 16 this is it! 11+5 also 16. So we take the first encountered
    # we dont have to check all numbers. We can check up to middle of the list coming from the right side of the list.
    if n%2!=0: return False
    primes = print_prime(n-2) # get primes list
    l = len(primes) # get length
    right = 0 # starting right element index
    left = l-1 # starting left element index
    counter = 0
    while counter <= l: # march from the leftmost element to the right
        while right < left:
            if primes[left]+primes[right] == n:
                return ("{} + {} = {}".format(primes[left], primes[right], n))
                #return True
            right += 1
        left -= 1
        counter+=1
    return False
# better than above
def sum_primes_even2(n): # each time subtract x from n and check if both x and n-x are prime. increase x
    if n%2!=0: return False

    x = 3
    x2 = 0
    while x < n:
        x2 = n - x
        if is_prime(x2) and is_prime(x):
            return ("{} + {} = {}".format(x, x2, n))
        x += 2
    return False

def gcd(m, n):
    save = n
    while m != 0:
        n = m
        m = save%m
        save = n
    return n


def main():
    #print(sum_n(10))
    #print(sum_odd(10))
    #print(interactive_sum())
    #print(division_bytwo(4096))
    #print(fibonacci(450))
    #windchill()
    #print(wind_index(45,40))
    #print(double_invest(5000, 0.05))
    #print(is_prime(5463458053)) #ex5
    #print(print_prime(1024)) # ex6
    #print(sum_primes_even2(4544))
    print(gcd(144,5463458052))




if __name__ == '__main__':
    main()
