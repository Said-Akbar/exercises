# exercise 1 from chapter 10. 01/19/2020 by SaidakbarP
# cannonball simulation and calculation of its max height
from math import sin, cos, radians

class Projectile:
    """docstring for Projectile."""
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        theta = radians(angle)
        self.ypos = height
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.ymax = 0

    def update(self, time):
        self.xpos = self.xpos + time*self.xvel                  # xvel is constant because we ignore wind resistance *o....ccco.....co*
        yvel1 = self.yvel - time * 9.8                          # yvel decreases each second by 9.8 m/s^2 because of gravity.
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0  # initially the ball goes up and then starts to go down eventually reaching the ground
        #print(self.ypos)
        if self.ypos > self.ymax:
            self.ymax = self.ypos
        self.yvel = yvel1
    def getY(self):
        return self.ypos
    def getX(self):
        return self.xpos
    def getYmax(self):
        return self.ymax
