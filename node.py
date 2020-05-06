# Class for the nodes
# 4/27/20
__author__ = "Jack Preble"


class Node:

    def __init__(self, row, col, height, open, f_cost, g_cost, h_cost):
        self.row = row
        self.col = col
        self.height = height
        self.open = open
        self.f_cost = f_cost
        self.g_cost = g_cost
        self.h_cost = h_cost