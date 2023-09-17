import numpy as np
import matplotlib.pyplot as plt

class OpticalTable:
    def __init__(self,length:float,width:float,gridspacing:float=1.0,scale:float=10):
        
        self.length = length
        self.width = width
        self.gridspacing = gridspacing
        self.scale = scale
        
        self.initialize_table(self.length,self.width)
        
        
    def initialize_table(self,length,width):
        plt.figure(figsize=(length*self.scale,width*self.scale),frameon=False)
        table_perimeter = np.array([[0,0,length,length,0],
                                    [0,width,width,0,0],])
        offset = np.array([[-1,-1,1,1,-1],
                           [-1,1,1,-1,-1]])*self.gridspacing/4
        
        table_perimeter = np.squeeze(table_perimeter + offset)
        

        plt.plot(table_perimeter[0],table_perimeter[1],
                 color="black")
        
        grid = [[],[]]
        for x in np.arange(0,length+self.gridspacing,self.gridspacing):
            for y in np.arange(0,width+self.gridspacing,self.gridspacing):
                grid[0].append(x)
                grid[1].append(y)
        
        minor_grid = [[],[]]
        for x in np.arange(self.gridspacing*1/2,length+self.gridspacing*1/2,self.gridspacing):
            for y in np.arange(self.gridspacing*1/2,width+self.gridspacing*1/2,self.gridspacing):
                minor_grid[0].append(x)
                minor_grid[1].append(y)
        
        plt.scatter(grid[0],grid[1],color="grey",alpha=0.5,s=10)
        plt.scatter(minor_grid[0],minor_grid[1],color="grey",alpha=0.5,s=5)
        
        # plt.axis("off")
        

    def draw(self):
        plt.title("Optical Table Layout")
        plt.xlim(-self.length/3,self.length*4/3)
        plt.ylim(-self.width/3,self.width*4/3)
        plt.tight_layout
        plt.show()
        