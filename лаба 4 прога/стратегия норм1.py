from abc import ABC, abstractmethod

# Интерфейс стратегии
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Конкретная стратегия "Умножение"
class MyltiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

# Конкретная стратегия "ДЕЛЕНИЕ"
class DivisionStrategy(Strategy):
    def execute(self, a, b):
        return a/b


class Calculator:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)

# Пример использования
calc = Calculator(MyltiplyStrategy())
print(calc.calculate(5, 3)) 

calc.set_strategy(DivisionStrategy())
print(calc.calculate(5, 3))   
