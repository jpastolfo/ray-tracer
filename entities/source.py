import matplotlib.pyplot as plt
import numpy as np

from .beam import Ray

class Source:
    def __init__(self,x:float,y:float,angle:float,color:str):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
    
    
    def generate_ray(self):
        ray = Ray(self.x,self.y,self.angle,self.color)
        return ray