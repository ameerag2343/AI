from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Traingle(Polygon):
    def sides(self):
        print("I Have 3 sides")

class Rectangle(Polygon):
    def sides(self):
        print("I have 4 sides")

T = Traingle()
T.sides()

R = Rectangle()
R.sides()

