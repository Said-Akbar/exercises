# exercise 1 from chapter 10. 01/19/2020 by SaidakbarP
# cannonball simulation and calculation of its max height
from projectile import Projectile # when importing modules make sure you are using filename and then class name
def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (meters/sec): "))
    h = float(input("Enter the initial height (meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t

    theta = radians(angle)

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:.1f} meters. Max height {1:.1f}".format(cball.getX(), cball.getYmax()))

if __name__=="__main__":
    main()
