import math
import matplotlib.pyplot as plt
from .base import Figure

class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def draw(self):
        fig, ax = plt.subplots()
        circle = plt.Circle((0, 0), self.radius, fill=False, color='blue')
        ax.add_patch(circle)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-self.radius * 1.2, self.radius * 1.2)
        ax.set_ylim(-self.radius * 1.2, self.radius * 1.2)
        plt.title(f"Circle (radius={self.radius})")
        plt.grid(True)
        plt.show()
