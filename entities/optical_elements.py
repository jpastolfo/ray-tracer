import matplotlib.pyplot as plt
import numpy as np

from .beam import Ray


class OpticalElement:
    def __init__(self,x:float,y:float,angle:float,size:float):
        self.x = x
        self.y = y
        self.angle = angle
        self.size = size
    
    
    def intersect():
        pass
    
    
    def draw():
        pass


class PlaneMirror(OpticalElement):
    def __init__(self,x:float,y:float,angle:float,size:float):
        super().__init__(x,y,angle,size)
        self.calculate_tangent_vector()
        self.calculate_normal_vector()
        self.draw()
    
    
    def calculate_tangent_vector(self):
        self.direction = [np.cos(np.radians(self.angle)),
                                 np.sin(np.radians(self.angle))]
    
    
    def calculate_normal_vector(self):
        self.normal = [-self.direction[1],self.direction[0]]
        
    
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
        dx = (self.size/2) * np.cos(np.radians(self.angle))
        dy = (self.size/2) * np.sin(np.radians(self.angle))
        plt.plot([self.x-dx, self.x+dx],[self.y-dy, self.y+dy],color="black")
        plt.arrow(self.x,self.y,*self.direction,color="green",width=0.1)
        plt.arrow(self.x,self.y,*self.normal,color="orange",width=0.1)
        