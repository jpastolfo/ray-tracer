from core.vector import Vector2D
from entities.table import OpticalTable

class Source:
    def __init__(
        self,
        table:OpticalTable,
        position:Vector2D,
        orientation:float = ...,
        wavelength:float = ...,
        color:str = ...,
        n_rays:int = ...,
        max_collisions:int = ...,
        linestyle:str = ...
    ) -> None: ...
    def generate_rays(self) -> list: ...
    
class PointSource(Source):
    def __init__(
        self,
        table,
        position:Vector2D,
        divergence:float,
        **kwargs
    ) -> None: ...
    def generate_rays(self) -> list: ...

class BoxSource(Source):
    def __init__(
        self,
        table:OpticalTable,
        position:Vector2D,
        divergence:float,
        dimension:Vector2D,
        **kwargs
    ) -> None: ...
    def draw(self) -> None: ...
    def get_vertices(self) -> Vector2D: ...
    def generate_rays(self) -> list: ...
