class Singleton:
    _instance = None  # Хранит единственный экземпляр класса

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Если экземпляр еще не создан
            cls._instance = super(Singleton, cls).__new__(cls)  # Создаем новый экземпляр
        return cls._instance  # Возвращаем единственный экземпляр

# Пример использования
s1 = Singleton()  # Создаем первый экземпляр
s2 = Singleton()  # Пытаемся создать второй экземпляр

print(s1 is s2)  # Проверяем, что оба экземпляра одинаковы (True)
