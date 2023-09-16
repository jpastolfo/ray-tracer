import matplotlib.pyplot as plt
import numpy as np


class OpticalElement:
    def __init__(self,x:float,y:float,angle:float,size:float):
        self._x = x
        self._y = y
        self._angle = angle
        self._size = size
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def angle(self):
        return self._angle
    
    @property
    def size(self):
        return self._size
    
    
    def draw():
        pass


class Mirror(OpticalElement):
    def __init__(self,x:float,y:float,angle:float,size:float):
        super().__init__(x,y,angle,size)
        self.draw()
    
    def draw(self):
        dx = (self.size/2) * np.cos(np.deg2rad(self.angle))
        dy = (self.size/2) * np.sin(np.deg2rad(self.angle))
        plt.plot([self.x-dx, self.x+dx],[self.y-dy, self.y+dy])