# A* Pathing Algorithm
# Apr. 6, 2020
__author__ = "Jack Preble"

import pygame
import matplotlib
import numpy as np

from drawMap import *

# Numpy tutorial (took stuff from it): https://likegeeks.com/numpy-array-tutorial/#Add-array-element

# using file: "Colorado_480x480.dat"

# Global Variables
avg = 0  # average height of all values
startz = 0  # height of start point
endz = 0  # height of end point
startList = []  # values of heights on the far right side of the map
endList = [] # values of heights on the far left side of the map
carryOn = True
add = np.array([])

# Quick Variables
startx = 480
endx = 0

#edit

# Working list of all values (organized into lists by x value)
data = np.loadtxt('Colorado_480x480.dat') # https://www.kaggle.com/questions-and-answers/27699

grid = np.array([])

# fits in somewhere: https://docs.scipy.org/doc/numpy/user/quickstart.html

def average():
    global avg

    avg = np.average(data)


def findStart():
    global avg, startList, startz

    y = 0

    average()

    for i in data:
        startList.append(int(i[-1]))


    startz = startList[min(range(len(startList)), key=lambda i: abs(startList[i] - avg))] # https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/


def findEnd():
    global avg, endList, endz

    average()

    for i in data:
        endList.append(int(i[1]))

    endz = endList[min(range(len(endList)), key=lambda i: abs(endList[i] - startz))] # https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/


'''def buildGrid():
    global grid, data, add

    for list in data:
        for e in list:
            np.append(add, np.where(e))
            continue
        np.append(add, np.where(list))

    np.append(grid, add)

    np.clear(add)'''

#https://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array


def main():
    global carryOn

    findStart()
    findEnd()

    '''while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # https://stackoverflow.com/questions/26822175/pygame-if-event-type-pygame-keydown-typeerror-int-object-is-not-callable/26822211
                carryOn = False'''

    h = np.array([])
    g = np.array([])

    np.append(h, np.asarray(np.where(data == endz)))

    for i in h:
        np.append(g, [i])

    print(h)
    print(g)

    '''print(avg)
    print(startList)
    print(endList)
    print(startz)
    print(endz)'''

if __name__ == "__main__":
    main()

