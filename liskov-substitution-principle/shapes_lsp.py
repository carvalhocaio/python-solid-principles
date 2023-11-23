from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


"""
Shape torna-se o tipo que pode ser substituído atráves de polimorfismo por Rectangle ou Square, que agora são irmão em 
vez de pai e filho. Observe que ambos os tipos de formas concretas possuem conjuntos distintos de atributos, métodos
inicializadores diferentes e poderiam implementar comportamentos ainda mais esperados. A única coisa que eles têm em 
comum é a capacidade de calcular sua área.

Como a função só se preocupa com o método .calculate_area(), não importa que as formas sejam diferentes. Esta é a 
essência do princípio da substituição de Liskov.
"""
