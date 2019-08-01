"""
level: 5 kyu
Link: https://www.codewars.com/kata/double-cola/train/python
Description:
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Write a program that will return the name of the person who will drink the n-th cola.
"""
def who_is_next(names, r):
    lname = len(names)
    # 5 ppl, 1st round 5 (2^0*5), 2nd 10 (2^1*5), 3rd 20 (2^2*5), 4th 40 (2^3*5), so
    # 5+10+20+40=75. 52 is in 4th round, thus, 40/5=8 for each, 35+8+8 and +8 is penny
    c =0
    x=0
    pos=-1
    if lname>=r: return names[r-1]
    
    while x<r: # calculate the sum up to 2^c*lname rounds
        x = x + (2**c)*lname
        c +=1
    prev = x - (2**(c-1))*lname
    
    while prev<r: # calculate the position
        prev += 2**(c-1)
        pos += 1
    
    return names[pos]
        
