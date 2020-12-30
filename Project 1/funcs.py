from math import *


def poundsToKG(pounds):
    return pounds * 0.453592


def getMassObject(object):
    if object == 't':
        return 0.1
    elif object == 'p':
        return 1.0
    elif object == 'r':
        return 3.0
    elif object == 'g':
        return 5.3
    elif object == 'l':
        return 9.07
    else:
        return 0.0


def getVelocityObject(distance):
    return sqrt(9.8 * distance/2)


def getVelocitySkater(massSkater, massObject, velObject):
    return (massObject * velObject) / massSkater
