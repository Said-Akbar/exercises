# Calculate the prime factors of a number. Level: 5 kyu. This took me many hours (10 hours) to figure out. I think I need to take an online course on algorithms. 
# description: https://www.codewars.com/kata/primes-in-numbers/train/python
def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n) # Find prime factors and create a list
        
    prime_dict = {}
    for i in factors:
        if i in prime_dict:
            prime_dict[i] += 1
        elif not (i in prime_dict):
            prime_dict[i] =1 # create a dictionary of each prime factor
    
    prime_word = ''          # create a string for final output  
    for a, b in sorted(prime_dict.items()):
        if int(b)==1:
            prime_word += '({})'.format(a)
        else:
            prime_word += '({}**{})'.format(a,b)

    return prime_word