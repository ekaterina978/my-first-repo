from abc import ABC, abstractmethod

# Базовые интерфейсы продуктов
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass  # Метод, который должен реализовать каждый продукт A

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass  # Метод, который должен реализовать каждый продукт B

# Конкретные продукты A
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

# Конкретные продукты B
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

# Базовый интерфейс фабрики
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass  # Метод для создания продукта A

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass  # Метод для создания продукта B

# Конкретные фабрики
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()  # Создает продукт A1

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()  # Создает продукт B1

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()  # Создает продукт A2

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()  # Создает продукт B2

# Пример использования
def client_code(factory: AbstractFactory) -> None:# Клиентский код работает с фабриками и продуктами только через абстрактные типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    product_a = factory.create_product_a()  # Создаем продукт A через фабрику
    product_b = factory.create_product_b()  # Создаем продукт B через фабрику
    print(product_a.useful_function_a())  # Используем продукт A
