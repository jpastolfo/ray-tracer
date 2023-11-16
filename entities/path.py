from typing import Any
from point import *

from dataclasses import dataclass

@dataclass
class Path2D:

    points : list
    
    def __init__(self,point:Point2D):
        self.points = [point]
    

    def append(self,point:Point2D):
        self.points.append(point)

    
    def __str__(self) -> str:
        return f"{type(self).__name__} with {len(self.points)} points."


@dataclass
class Path3D:

    points : list

    def __init__(self,point:Point3D):
        self.points = [point]
    

    def append(self,point:Point3D):
        self.points.append(point)

    
    def __str__(self) -> str:
        return f"{type(self).__name__} with {len(self.points)} points"
    