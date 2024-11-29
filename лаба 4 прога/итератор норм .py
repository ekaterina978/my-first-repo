from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def has_next(self): #метод возвр true если есть некст элемент иначе false
        pass

    @abstractmethod
    def next(self):# возвращает некст элемент в колекции 
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0 # инициализация индекса с 0 чтобы начать с 1 элемента 

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        item = self._collection[self._index]
        self._index += 1
        return item

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return ConcreteIterator(self._items)


