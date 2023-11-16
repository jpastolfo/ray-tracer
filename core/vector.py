class Vector2D:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    
    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}"
            f"(x={self.x}, "
            f"y={self.y})"
        )
    

    def __setattr__(self,__name:str,__value:Any) -> None:
         self.__dict__[f"{__name}"] = float(__value)


class Vector3D:
    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    
    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}"
            f'(x={self.x}, '
            f'y={self.y}, '
            f"z={self.z})"
        )
    

    def __setattr__(self,__name:str,__value:Any) -> None:
         self.__dict__[f"{__name}"] = float(__value)