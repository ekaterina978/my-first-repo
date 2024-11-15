from abc import ABC, abstractmethod

# Базовый интерфейс продукта
class Product(ABC):
    @abstractmethod
    def operation(self) -> str: # метод который возвращает строку 
        pass  # Метод, который должен реализовать каждый продукт

# Конкретные продукты
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"

# Базовый интерфейс создателя
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass  # Метод для создания продукта

    def some_operation(self) -> str:
        product = self.factory_method()  # Создаем продукт через фабричный метод
        return f"Creator: The same creator's code has just worked with {product.operation()}"

# Конкретные создатели
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()  # Создает продукт A

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()  # Создает продукт B

# Пример использования
creator_a = ConcreteCreatorA()
print(creator_a.some_operation())  # Используем создателя A

creator_b = ConcreteCreatorB()
print(creator_b.some_operation())  # Используем создателя B
