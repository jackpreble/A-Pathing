
class ElevationMap:
    grid = []
    min_elevation = None
    max_elevation = None
    difference = None
    step_value = None
    colors = None
    '''colors = [("rose",(255, 0, 127)), ("magenta",(255, 0, 255)),
                ("violet",(127, 0, 255)), ('blue',(0, 0, 255)),
                ('azure', (0, 127, 255)), ('cyan',(0, 255, 255)),
                ('spring green',(0, 255, 127)), ('green',(0, 255, 0)),
                ('chartreuse green',(127, 255, 0)), ('yellow',(255, 255, 0)),
                ('orange',(255, 127, 0)), ('red',(255, 0, 0))]'''

    # constructor for class ElevationMap
    def __init__(self, filename):
        self.colors = [(255, 0, 127), (255, 0, 255), (127, 0, 255), (0, 0, 255),
         (0, 127, 255), (0, 255, 255), (0, 255, 127), (0, 255, 0), (127, 255, 0),
         (255, 255, 0), (255, 127, 0), (255, 0, 0)]
        file = open(filename)
        for line in file:
            line = line.strip()
            line = line.split('   ')
            self.grid.append(line)
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = int(self.grid[r][c])
        file.close()
        self.find_min_max()
        print('DEBUG map width:', len(self.grid))
        print('DEBUG max height:', len(self.grid[0]))

    # used for testing/debugging purposes
    def find_min_max(self):
        self.min_elevation = self.grid[0][0]
        self.max_elevation = self.grid[0][0]
        for row in self.grid:
            for item in row:
                if item < self.min_elevation:
                    self.min_elevation = item
                if item > self.max_elevation:
                    self.max_elevation = item
        print('Min elevation:', self.min_elevation, ' | Max elevation:', self.max_elevation)
        self.difference = (self.max_elevation-self.min_elevation)
        print('Difference:', self.difference)
        self.step_value = self.difference//(len(self.colors)-1)
        print('Step blocks:', self.step_value)

    # return a 2D list of colors based on elevation profile
    def get_color_map(self):
        color_grid = []
        for row in range(len(self.grid)):
            color_grid.append([])
            for elev in self.grid[row]:
                color_grid[row].append(self.get_color(elev))
        return color_grid

    # return a color based on elevation
    def get_color(self, elev):
        height = self.max_elevation
        index = 0
        while height > self.min_elevation and index < 12:
            if height <= elev and height >= height-self.step_value:
                return self.colors[index]
            else:
                index += 1
                height -= self.step_value
        return (0,0,0)
