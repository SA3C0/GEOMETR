from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def draw(self):
        """Visualize figure using matplotlib"""
        pass
