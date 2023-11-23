from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2


"""
Neste código, a classe Shape foi completamente refatorada, transformando-a em uma classe base abstrata (ABC). Esta
classe fornece a interface (API) necessária para qualquer forma que seja definida. Essa interface consiste em um
atributo .shape_type e um método .calculate_area() que devem ser substituídos nas subclasses.

Obs: O exemplo acima usa o ABC do Python para fornecer o que é chamado de herança de interface. Neste tipo de herança, 
as subclasses herdam interfaces em vez de funcionalidade. Por outro lado, quando as classes herdam funcionalidades, elas
recebem herança de implementação.

Esta atualização fecha a classe para modificações. Agora é possível adicionar novas formas ao design da classe sem a 
necessidade de modificar Shape. Em todos os casos, é necessário implementar a interface necessária, o que também torna
a classe polimórfica. 
"""
