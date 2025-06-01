from .circle import Circle
from .triangle import Triangle

def figure_factory(shape: str, *args):
    shape = shape.lower()
    if shape == 'circle':
        if len(args) != 1:
            raise ValueError("Circle requires exactly 1 argument (radius)")
        return Circle(args[0])
    elif shape == 'triangle':
        if len(args) != 3:
            raise ValueError("Triangle requires exactly 3 arguments (sides)")
        return Triangle(*args)
    else:
        raise ValueError(f"Unsupported shape type: {shape}")
