import matplotlib.pyplot as plt
import numpy as np

from .beam import Ray

class Source:
    def __init__(self,table,x:float,y:float,orientation:float,wavelength:list,
                 color:str="red",n_rays:int=1):
        self.table = table
        self.x = x
        self.y = y
        self.orientation = orientation
        self.wavelength = wavelength
        self.color = color
        self.n_rays = n_rays

        self.table.append_source(self)

    
    def generate_rays(self):
        pass
    

class PointSource(Source):
    def __init__(self,table,x:float,y:float,orientation:float,wavelength:float,divergence:float,**kwargs):
        super().__init__(table,x,y,orientation,wavelength,**kwargs)
        self.divergence = divergence
    
    
    def generate_rays(self):
        angles = np.linspace(self.orientation + self.divergence/2,
                             self.orientation - self.divergence/2,
                             self.n_rays)
        rays = [Ray(self.x,self.y,angle,self.wavelength,self.color,source=self) for angle in angles]
        return rays
    

class BoxSource(Source):
    def __init__(self,table,x:float,y:float,orientation:float,wavelength:list,**kwargs):
        super().__init__(table,x,y,orientation,wavelength,**kwargs)
        
        
        self.draw()


    def draw(self):
        plt.plot()
        pass


    def get_vertices(self):
        pass
