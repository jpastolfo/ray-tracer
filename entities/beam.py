import matplotlib.pyplot as plt
from entities.optical_elements import OpticalElement

class Beam:
    def __init__(self,color):
        self.__color = color
        self.__path = []
    
    
    def append_to_path(self,*elements:OpticalElement):
        for element in elements:
            self.__path.append(element)
    
    
    def trace(self):
        for idx,optical_element in enumerate(self.__path[:-1]):
            next_optical_element = self.__path[idx+1]
            print(optical_element.x)
            plt.plot([optical_element.x,next_optical_element.x],
                     [optical_element.y,next_optical_element.y],
                     color=self.__color)