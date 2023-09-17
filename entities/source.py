import matplotlib.pyplot as plt
import numpy as np

from .beam import Ray

class Source:
    def __init__(self,x:float,y:float,angle:float,color:str,
                 n_rays:int=1):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.n_rays = n_rays

    
    def generate_ray(self):
        ray = Ray(self.x,self.y,self.angle,self.color)
        return ray
    

class Lamp(Source):
    def __init__(self,x:float,y:float,color:str,
                 n_rays:int=1):
        super().__init__(x,y,0,color,n_rays)
        
    def generate_rays(self):
        rays = [Ray(self.x,self.y,angle,self.color) for angle in np.linspace(0,360,self.n_rays)]
        return rays


class DivergentSource(Source):
    def __init__(self,x:float,y:float,divergence:float,color:str,n_rays:int=1):
        super().__init__(x,y,0,color,n_rays=n_rays)
        
        self.divergence = divergence
    
    
    def generate_rays(self):
        angles = np.linspace(-self.divergence/2,self.divergence/2,self.n_rays)
        rays = [Ray(self.x,self.y,angle,self.color) for angle in angles]
        return rays