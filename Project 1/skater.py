# Project 1
#
# Name: Forrest Dudley
# Instructor: Workman
# Section: 11

from math import *
from funcs import *

def main():
    massSkater = poundsToKG(int(input("How much do you weigh (pounds)? ")))
    distance = int(input("How far away is your professor (meters)? "))
    massObject = getMassObject(input("Will you throw a rotten (t)omato, bananacream (p)ie, (r)ock, "
                                     "(l)ight saber, or lawn (g)nome? "))
    velocitySkater = getVelocitySkater(massSkater, massObject, getVelocityObject(distance))

    print("\nNice throw! ", end="")
    if massObject <= 0.1:
        print("You're going to get an F!")
    elif 0.1 < massObject <= 1.0:
        print("Make sure your professor is OK.")
    else:
        if distance < 20:
            print("How far away is the hospital?")
        else:
            print("RIP professor.")

    print("Velocity of Skater: %.3f m/s" %velocitySkater)
    if velocitySkater < 0.2:
        print("My grandmother skates faster than you!")
    elif 0.2 <= velocitySkater < 1.0:
        return
    else:
        print("look out for that railing!!!")


if __name__ == '__main__':
    main()
