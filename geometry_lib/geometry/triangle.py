import math
import matplotlib.pyplot as plt
from .base import Figure
from .utils import is_right_triangle

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        self.a = a
        self.b = b
        self.c = c

        if not self._is_valid():
            raise ValueError("Invalid triangle sides")

    def _is_valid(self) -> bool:
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return is_right_triangle(self.a, self.b, self.c)

    def draw(self):
        A = (0, 0)
        B = (self.c, 0)

        x = (self.b**2 + self.c**2 - self.a**2) / (2 * self.c)
        y = math.sqrt(abs(self.b**2 - x**2))
        C = (x, y)

        xs, ys = zip(A, B, C, A)

        plt.figure()
        plt.plot(xs, ys, 'r-o')
        plt.axis('equal')
        plt.title(f"Triangle (a={self.a}, b={self.b}, c={self.c})")
        plt.grid(True)
        plt.show()
