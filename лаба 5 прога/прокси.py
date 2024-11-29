class Animal:
    def request(self):
        return "Запрос к реальному объекту."

class Proxy:
    """Прокси-класс, который контролирует доступ к реальному объекту."""
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Прокси: Выполняю предварительные действия.")
        result = self._real_subject.request()  # Перенаправляем запрос к реальному объекту
        print("Прокси: Выполняю последующие действия.")
        return result
