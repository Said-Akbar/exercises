print(-10//3) # answer is -4 coz of floor division. 10/3 = 3.33 -> flooring leads to 4. So, -4 for negative.
print(round(314.1592, -1)) # 310. rounds the integer part, -1 means round to the tenth.
print(-10%3) # -4*3=-12 => -12+x=-10 => x=2
print(10//-3) # -4
print(10%-3) # -4*-3=12 => 12+x = 10 => x=-2
print(-10//-3) # 3

import math
def vol_a_sphere(r):
    vol = 4/3 * math.pi * r**3
    area = 4 * math.pi *r**2
    return vol, area
print(vol_a_sphere(int(input("Enter radius of a sphere: "))))

def distance_lightning(time):
    distance = time*1100/5280
    print("The distance is: ", round(distance,4), " miles")
distance_lightning(int(input("Enter the seconds elapsed: ")))

def pi_approx(terms):
    p = 0
    for i in range(1, 2*terms, 4):
        p = p + 4/i - 4/(i+2)
    return p
p=pi_approx(int(input("Enter term numbers to calculate pi: ")))
print("Calculated pi: ", p)
print("difference from actual pi: ", math.pi-p)

def fibonnacci_swap(terms):
    cur, prev = 1, 1
    for i in range(terms-2):
        cur, prev = cur + prev, cur
    return cur

print(fibonnacci_swap(int(input("Enter fibonnacci terms (math): "))))

def fibonnacci(terms):

    x=0
    f=1
    for i in range(terms+1):
        x = x + f
        f = x - f
    return f
print(fibonnacci(int(input("Enter fibonnacci terms (math): "))))
# check for time efficiency of two fibonacci functions later
