class Product:
    def __init__(self):
        self.parts = [] # инициализируем список parts

    def add(self, part: str) -> None: # add добавляет новые строку в список
        self.parts.append(part)

    def list_parts(self) -> None: # выводит все части продукта обЪединяя их в строку 
        print(f"Product parts: {', '.join(self.parts)}")

class Builder(ABC):
    @abstractmethod
    def build_part_a(self) -> None:
        pass

    @abstractmethod
    def build_part_b(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Product:
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()  # Создаем новый экземпляр продукта

    def build_part_a(self) -> None:
        self.product.add("Part A")  # Добавляем часть A к продукту

    def build_part_b(self) -> None:
        self.product.add("Part B")  # Добавляем часть B к продукту

    def get_result(self) -> Product:
        return self.product  # Возвращаем готовый продукт
