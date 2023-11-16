import numpy as np
import matplotlib.pyplot as plt

class OpticalTable:
    def __init__(self,dimension:"tuple[float,float]",gridspacing:float=1.0,scale:float=10):
        
        self.length, self.width = dimension
        self.gridspacing = gridspacing
        self.scale = scale

        self.sources = []
        self.optical_elements = []
        
        self.initialize_table()
        
        
    def initialize_table(self):
        plt.figure(figsize=(self.length*self.scale,self.width*self.scale),frameon=False)
        table_perimeter = np.array([[0,0,self.length,self.length,0],
                                    [0,self.width,self.width,0,0],])
        offset = np.array([[-1,-1,1,1,-1],
                           [-1,1,1,-1,-1]])*self.gridspacing/4
        
        table_perimeter = np.squeeze(table_perimeter + offset)
        

        plt.plot(table_perimeter[0],table_perimeter[1],
                 color="black")
        
        grid = [[],[]]
        for x in np.arange(0,self.length+self.gridspacing,self.gridspacing):
            for y in np.arange(0,self.width+self.gridspacing,self.gridspacing):
                grid[0].append(x)
                grid[1].append(y)
        
        plt.scatter(grid[0],grid[1],color="grey",alpha=0.5,s=2)
        
        # plt.axis("off")

    
    def append_source(self,*sources):
        for source in sources:
            self.sources.append(source)
    

    def append_optical_element(self,*optical_elements,verbose:bool=False):
        for element in optical_elements:
            if verbose: print(element)
            self.optical_elements.append(element)
        

    def draw(self):
        plt.title("Optical Table Layout")
        plt.xlim(-self.length/3,self.length*4/3)
        plt.ylim(-self.width/3,self.width*4/3)
        plt.tight_layout
        plt.show()
        