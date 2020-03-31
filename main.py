# A* Pathing Algorithm
# Apr. 6, 2020
__author__ = "Jack Preble"

import pygame
import matplotlib
import numpy as np

from drawMap import *

# using file: "Colorado_480x480.dat"

# Global Variables
avg = 0  # average height of all values
startz = 0  # height of start point
endz = 0  # height of end point
startList = []  # values of heights on the far right side of the map
endList = [] # values of heights on the far left side of the map

# Quick Variables
startx = 480
endx = 0

#edit

# Working list of all values (organized into lists by x value)
xyz = np.loadtxt('Colorado_480x480.dat') # https://www.kaggle.com/questions-and-answers/27699



# fits in somewhere: https://docs.scipy.org/doc/numpy/user/quickstart.html

def average():
    global avg

    avg = np.average(xyz)


def findStart():
    global avg, startList, startz

    average()

    for i in xyz:
        startList.append(int(i[-1]))

    startz = startList[min(range(len(startList)), key=lambda i: abs(startList[i] - avg))] # https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/

def findEnd():
    global avg, endList, endz

    average()

    for i in xyz:
        endList.append(int(i[1]))

    endz = endList[min(range(len(endList)), key=lambda i: abs(endList[i] - startz))] # https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/


def main():
    global gray

    findStart()
    findEnd()
    #draw_map(gray,px=1)

    print(avg)
    print(startList)
    print(endList)
    print(startz)
    print(endz)


if __name__ == "__main__":
    main()
