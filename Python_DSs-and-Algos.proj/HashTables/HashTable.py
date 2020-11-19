class HashTable:
    __count = 0
    __capacity = 0
    __probeFactor = 0
    __capacityTreshold = 0
    __data = []

    def __init__(self):
        self.__count = 0
        self.__capacity = 10
        self.__data = [None] * self.__capacity
        self.__probeFactor = 1
        self.__capacityTreshold = round(self.__capacity * (2 / 3), 0)

    def __probe(self, factor: int) -> int:
        return factor * self.__probeFactor

    def __indexOf(self, key: str) -> int:
        hashed = self.key_hash(key)
        index = hashed
        counter = 1
        while True:
            if self.__data[index] is None:
                return -1
            if self.__data[index][0] == key:
                break
            index = (hashed + self.__probe(counter)) % self.__capacity
            counter += 1
        return index

    def __upsize(self):
        self.__count = 0
        self.__capacity *= 2
        self.__capacityTreshold = round(self.__capacity * (2 / 3), 0)
        oldData = self.__data
        self.__data = [None] * self.__capacity
        for i in range(len(oldData)):
            if oldData[i] is not None:
                self.add(oldData[i][0], oldData[i][1])

    def __get(self, key):
        index = self.__indexOf(key)
        if index == -1:
            raise KeyError
        return self.__data[index]
        

    def key_hash(self, key: str) -> int:
        if isinstance(key, str) == False:
            raise ValueError
        if len(key) == 0:
            raise ValueError
        hashed = hash(key)
        if hashed < 0:
            hashed = -(hashed)
        return hashed % self.__capacity

    def add(self, key: str, value):
        hashed = self.key_hash(key)
        index = hashed
        counter = 1
        while self.__data[index] is not None:
            if self.__data[index][0] == key:
                self.__data[index] = (key, value)
                return
            index = (hashed + self.__probe(counter)) % self.__capacity
            counter += 1
        self.__data[index] = (key, value)
        self.__count += 1
        if self.__count == self.__capacityTreshold:
            self.__upsize()

    def remove(self, key: str):
        index = self.__indexOf(key)
        if index == -1:
            raise KeyError
        self.__data[index] = None
        self.__count -= 1


    def getValue(self, key: str):
        return self.__get(key)[1]

    def exists(self, key: str):
        if self.__indexOf(key) == -1:
            return False
        return True

    def getAt(self, index: int):
        if index < 0 or index > self.__capacity - 1:
            raise IndexError
        return self.__data[index]

    def capacity(self) -> int:
        return self.__capacity

    def length(self) -> int:
        return self.__count



