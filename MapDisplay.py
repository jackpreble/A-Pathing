import pygame
from pygame import *
#from random import randint
import sys
from ElevationMap import *

def main():
    pygame.init()
    BLACK = (0, 0, 0)
    myGrid = ElevationMap('Colorado_480x480.dat')
    #myGrid.find_min_max()
    colors = myGrid.get_color_map()
    win = pygame.display.set_mode((len(colors)*2, len(colors[0])*2))  # based on map size
    print('DEBUG window size is', len(colors), 'x', len(colors[0]))
    for r in range(len(colors)):
        for c in range(len(colors[r])):
            pygame.draw.rect(win, colors[r][c], (r*2, c*2, 2, 2))
    pygame.display.update()

    while True:
        #win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        #pygame.display.flip()

if __name__ == '__main__':
    main()