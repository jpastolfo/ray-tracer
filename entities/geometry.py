import numpy as np
import matplotlib.pyplot as plt


class Box:
    def __init__(self, table: object, x: float, y: float, orientation :float, length: float, width: float) -> object:
        self.table = table
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = length
        self.width = width
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
