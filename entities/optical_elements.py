import matplotlib.pyplot as plt
import numpy as np

from entities.beam import Ray

from .beam import Ray


class OpticalElement:
    def __init__(self,table,x:float,y:float,orientation:float,size:float):
        self.table = table
        self.x = x
        self.y = y
        self.orientation = orientation
        self.size = size

        self.table.append_optical_element(self)
    
    
    def intersect():
        pass
    
    
    def draw():
        pass


class PlaneMirror(OpticalElement):
    def __init__(self,table,x:float,y:float,orientation:float,size:float):
        super().__init__(table,x,y,orientation,size)
        self.direction = self.calculate_tangent_vector(self.orientation)
        self.normal = self.calculate_normal_vector(self.direction)
        self.draw()
    
    @staticmethod
    def calculate_tangent_vector(orientation):
        return [np.cos(np.radians(orientation)),
                np.sin(np.radians(orientation))]
    
    @staticmethod
    def calculate_normal_vector(direction):
        return [-direction[1],direction[0]]
        
    
    def intersect(self,ray:Ray):
        denominator = ray.direction[0]*self.direction[1] - ray.direction[1]*self.direction[0]
            
        if denominator == 0 : return np.inf
        
        numerator = (self.x-ray.x)*self.direction[1] - (self.y-ray.y)*self.direction[0]
        numerator2 = (self.x-ray.x)*ray.direction[1] - (self.y-ray.y)*ray.direction[0]

        t = numerator/denominator
        u = numerator2/denominator
        print(f"t: {t}, u: {u}")
        if t > 1e-6 and abs(u) <= self.size/2: return t
        return np.inf
    
    
    def draw(self):
        dx = (self.size/2) * np.cos(np.radians(self.orientation))
        dy = (self.size/2) * np.sin(np.radians(self.orientation))
        plt.plot([self.x-dx, self.x+dx],[self.y-dy, self.y+dy],color="black")
        #plt.arrow(self.x,self.y,*self.direction,color="green",width=0.001)
        #plt.arrow(self.x,self.y,*self.normal,color="orange",width=0.001)


class Dicroic(PlaneMirror):
    def __init__(self,table,x:float,y:float,orientation:float,size:float,wavelength_range:list):
        super().__init__(table,x,y,orientation,size)
        self.wavelength_range = wavelength_range
    
    def intersect(self, ray: Ray):
        if self.wavelength_range[0] <= ray.wavelength <= self.wavelength_range[1]:
            return super().intersect(ray)
        return np.inf
    

class BeamSplitter(PlaneMirror):
    def __init__(self,x:float,y:float,orientation:float,size:float):
        super().__init__(x,y,orientation,size)


    def intersect(self, ray: Ray):
        transmitted_ray = Ray(ray.x,ray.y,ray.orientation,ray.wavelength,ray.color,source=ray.source)
        transmitted_ray.x += ray.direction[0]*1e3
        transmitted_ray.y += ray.direction[1]*1e3
        transmitted_ray.trace()
        transmitted_ray.draw()
        return super().intersect(ray)
        