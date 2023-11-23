from math import pi


class Shapes:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


"""
Imagine que você precisa adicionar uma nova forma, talvez um quadrado. A opção aqui é adicionar outra cláusula elif a
.__init__() e a .calculate_area() para que você possa atender aos requisitos de um quadrado.

Ter que fazer essas alterações para criar novas formas significa que sua classe está aberta a modificações. Isso viola o
princípio aberto-fechado.
"""
