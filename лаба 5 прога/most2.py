class AbstractFigure():
    """Общая реализация Фигуры"""
    def __init__(self, ImplementColoRClass):
        self.bridge_color = ImplementColoRClass
        
class Oval(AbstractFigure):
    def draw(self):
        print(f"Нарисовать  овал цветом {self.bridge_color.color}")
        
class Square(AbstractFigure):
    def draw(self):
        print(f"Нарисовать  Квадрат цветом {self.bridge_color.color}")

class AbstractLine(): # мост для работы с цветов в абстрактфигур
    def __init__(self):
        self.color = "White"

    def info_color(self):
        print(f"My color {self.color}")

class PinkLine(AbstractLine):
    def __init__(self):
        super().__init__()
        self.color = "Pink"


class RedLine(AbstractLine):
    def __init__(self):
        super().__init__()
        self.color = "Red"


class BlackLine(AbstractLine):
    def __init__(self):
        super().__init__()
        self.color = "Black"


