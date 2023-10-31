import numpy as np
import matplotlib.pyplot as plt


class Box:
    def __init__(self,table:object,position:tuple[float,float],orientation:float,dimension:tuple[float,float]) -> object:
        self.table = table
        self.x,self.y = position
        self.orientation = orientation
        self.length,self.width = dimension
        self.draw()

    def draw(self):
        plt.plot(*self.get_vertices(), color="black")

    def get_vertices(self):
        x = np.array([1, 1, -1, -1, 1]) * self.length / 2
        y = np.array([1, -1, -1, 1, 1]) * self.width / 2
        if self.orientation != 0.0:
            x_rotated = x * np.cos(np.radians(self.orientation)) - y * np.sin(np.radians(self.orientation))
            y_rotated = x * np.sin(np.radians(self.orientation)) + y * np.cos(np.radians(self.orientation))
            x = x_rotated; y = y_rotated
        x += self.x; y += self.y
        return x, y
