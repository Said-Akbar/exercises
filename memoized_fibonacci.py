# Memoized Fibonacci
# link: https://www.codewars.com/kata/memoized-fibonacci/python
def fibonacci(n, table=[0,1]):
    if n<2:               # this if statement makes sure we don't end the recursion one step early
        return 1
    elif n<=(len(table)): # if value already exists in th table, return that
        return table[n-1]
    else:                 # else calculate the sum of n-1 and n-2 elements of the table and append it
        x = fibonacci(n-1) + fibonacci(n-2)
        table.append(x) 
    return x