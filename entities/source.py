import matplotlib.pyplot as plt
import numpy as np

from .beam import Ray

class Source:
    def __init__(self,table,x:float,y:float,
                 orientation:float=0.0,wavelength:float=500.0,
                 color:str="red",n_rays:int=1,max_collisions:int=10,
                 linestyle:str="solid"):
        self.table = table
        self.x = x
        self.y = y
        self.orientation = orientation
        self.wavelength = wavelength
        self.color = color
        self.n_rays = n_rays
        self.max_collisions = max_collisions
        self.linestyle = linestyle

        self.table.append_source(self)

    
    def generate_rays(self):
        pass
    

class PointSource(Source):
    def __init__(self,table,x:float,y:float,divergence:float,**kwargs):
        super().__init__(table,x,y,**kwargs)
        self.divergence = divergence
    
    
    def generate_rays(self):
        angles = np.linspace(self.orientation + self.divergence/2,
                             self.orientation - self.divergence/2,
                             self.n_rays)
        rays = [Ray(self.x,self.y,angle,self.wavelength,self.color,source=self,max_collisions=self.max_collisions,linestyle=self.linestyle) for angle in angles]
        return rays
    

class BoxSource(Source):
    def __init__(self,table,x:float,y:float,divergence:float,length:float,width:float,**kwargs):
        super().__init__(table,x,y,**kwargs)
        self.divergence = divergence
        self.length = length
        self.width = width
        
        self.draw()


    def draw(self):
        plt.plot(*self.get_vertices(),color="black")


    def get_vertices(self):
        x = np.array([1,1,-1,-1,1])*self.length/2
        y = np.array([1,-1,-1,1,1])*self.width/2
        if self.orientation != 0.0:
            x_rotated = x * np.cos(np.radians(self.orientation)) - y * np.sin(np.radians(self.orientation))
            y_rotated = x * np.sin(np.radians(self.orientation)) + y * np.cos(np.radians(self.orientation))
            x = x_rotated; y = y_rotated
        x += self.x; y += self.y
        
        return x, y
    

    def generate_rays(self):
        angles = np.linspace(self.orientation + self.divergence/2,
                             self.orientation - self.divergence/2,
                             self.n_rays)
        
        x_ray = self.length/2; y_ray = 0.0
        if self.orientation != 0.0:
            x_rotated = x_ray * np.cos(np.radians(self.orientation)) - y_ray * np.sin(np.radians(self.orientation))
            y_rotated = x_ray * np.sin(np.radians(self.orientation)) + y_ray * np.cos(np.radians(self.orientation))
            x_ray = x_rotated; y_ray = y_rotated

        x_ray += self.x; y_ray += self.y

        rays = [Ray(x_ray,y_ray,angle,
                    self.wavelength,self.color,source=self,max_collisions=self.max_collisions) for angle in angles]
        return rays
