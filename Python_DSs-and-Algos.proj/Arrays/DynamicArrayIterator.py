class DynamicArrayIterator:
    def __init__(self, items, count):
        self.__items = items
        self.__index = 0
        self.__count = count
    
    def __next__(self):
        if (self.__index == self.__count):
            raise StopIteration
        item = self.__items[self.__index]
        self.__index += 1
        return item
