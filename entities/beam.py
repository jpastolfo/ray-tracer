import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass

@dataclass
class Path:
    x : list
    y : list
    def __init__(self,x:float,y:float):
        self.x = [x]
        self.y = [y]
    
    def append(self,x:float,y:float):
        self.x.append(x)
        self.y.append(y)
    

class Ray:
    def __init__(self,x,y,angle,color):
        self.x = x
        self.y = y
        self.calculate_direction(angle)
        self.color = color
        self.path = Path(self.x,self.y)
        self.max_collisions = 10
    
    
    def calculate_direction(self,angle):
        self.direction = [np.cos(np.radians(angle)),
                          np.sin(np.radians(angle))]
            
    
    def trace(self,objects):
        collisions = 0
        while collisions < self.max_collisions:
            distances = [element.intersect(self) for element in objects]
            nearest_element = None
            min_distance = np.inf
            print(f"Distances: {distances}")
            
            for index, distance in enumerate(distances):
                if distance and distance < min_distance:
                    min_distance = distance
                    nearest_element = objects[index]
                
            print(f"Nearest Element: {nearest_element}")
            print(f"Minimum Distance: {min_distance}")
            
            if nearest_element == None:
                self.path.append(self.x + self.direction[0]*1e3,
                                 self.y + self.direction[1]*1e3)
                break
            
            self.update_beam(nearest_element,min_distance)
            collisions += 1
            
    
    def reflect(self,element):
        dir_x = self.direction[0] - 2*np.dot(self.direction,element.normal)*element.normal[0]
        dir_y = self.direction[1] - 2*np.dot(self.direction,element.normal)*element.normal[1]
        self.direction = [dir_x,dir_y]
        
    
    def update_beam(self,element,distance):
        self.x += self.direction[0]*(distance)
        self.y += self.direction[1]*(distance)
        self.path.append(self.x,self.y)
        # self.x += 1e-5; self.y += 1e-5
        self.reflect(element)
        print("UPDATED")
        print(self.direction)
        print(self.x,self.y)
    
    
    def draw(self):
        print(self.path)
        plt.plot(self.path.x,self.path.y,color=self.color)