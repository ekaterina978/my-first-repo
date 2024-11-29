class Object:
    def request(self):
        return "Целевой запрос."

class Adaptee:
    def specific_request(self):
        return "Запрос от адаптируемого класса."

class Adapter(Object):
    """Адаптер, который связывает целевой класс и адаптируемый класс."""
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        # Преобразуем запрос из адаптируемого класса в целевой
        return self._adaptee.specific_request()

