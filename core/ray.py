from vector import Vector2D


class Ray2D:
    def __init__(self,origin:Vector2D,direction:Vector2D):
        self.origin = origin
        self.direction = direction






    def __str__(self) -> str:
        pass


    def __repr__(self) -> str:
        pass




class Ray2D:
    def __init__(self,origin:"tuple[float,float]",orientation:float,wavelength:float,
                 color:str,source=None,max_collisions:int=10,linestyle:str="solid"):
        
        self.x,self.y = position
        self.orientation = orientation
        self.calculate_direction(self.orientation)
        self.wavelength = wavelength 
        self.color = color
        self.path = Path(self.x,self.y,self.direction)
        self.max_collisions = max_collisions
        self.source = source
        self.linestyle = linestyle

    
    def calculate_direction(self,angle):
        self.direction = [np.cos(np.radians(angle)),
                          np.sin(np.radians(angle))]
            
    
    def trace(self,ignore_first_element=None, verbose:bool=False):
        table = self.source.table
        objects = table.optical_elements if table.optical_elements != None else []
        if ignore_first_element != None:
            objects.remove(ignore_first_element)
        if verbose: print(objects)
        
        collisions = 0
        while collisions < self.max_collisions:
            distances = [element.intersect(self) for element in objects]
            nearest_element = None
            min_distance = np.inf
            if verbose: print(f"Distances: {distances}")
            
            for index, distance in enumerate(distances):
                if distance and distance < min_distance:
                    min_distance = distance
                    nearest_element = objects[index]

            if verbose:   
                print(f"Nearest Element: {nearest_element}")
                print(f"Minimum Distance: {min_distance}")
            
            if nearest_element == None:
                self.path.append(self.x + self.direction[0]*1e3*1e-3,
                                 self.y + self.direction[1]*1e3*1e-3,
                                 self.direction)
                break
            
            self.update_beam(nearest_element,min_distance)
            collisions += 1
            
    
    def reflect(self,element):
        dir_x = self.direction[0] - 2*np.dot(self.direction,element.normal)*element.normal[0]
        dir_y = self.direction[1] - 2*np.dot(self.direction,element.normal)*element.normal[1]
        self.direction = [dir_x,dir_y]
        
    
    def update_beam(self,element,distance,verbose:bool=False):
        self.x += self.direction[0]*(distance)
        self.y += self.direction[1]*(distance)
        self.path.append(self.x,self.y,self.direction)
        self.reflect(element)
        if verbose:
            print("UPDATED")
            print(self.direction)
            print(self.x,self.y)
    
    
    def draw(self,verbose:bool=False):
        if verbose: print(self.path)
        plt.plot(self.path.x,self.path.y,color=self.color,linestyle=self.linestyle)