from abc import ABC, abstractmethod

# Базовый класс обработчика
class Person(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

# Конкретный обработчик "Обработчик A"
class ConcretePersonA(Person):
    def handle(self, request):
        if request == "A":
            print("Обработчик A обработал запрос.")
        else:
            super().handle(request)

# Конкретный обработчик "Обработчик B"
class ConcretePersonB(Person):
    def handle(self, request):
        if request == "B":
            print("Обработчик B обработал запрос.")
        else:
            super().handle(request)

