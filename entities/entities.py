import matplotlib.pyplot as plt
import numpy as np


class Source:
    def __init__(self,x:float,y:float,angle:float):
        self._x = x
        self._y = y
        self._angle = angle
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def angle(self):
        return self._angle
