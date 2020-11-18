class ArrayQ:
    __length = 0
    __maxCap = 6
    __data = []
    def __init__(self):
        self.__data = [None]*self.__maxCap
    def getSize(self):
        return self.__length
    def isEmpty(self):
        return self.__length == 0
    def isFull(self):
        return self.__length == self.__maxCap
    def getAt(self, index):
        if index < 0 or index > self.__length:
            raise Exception("Index out of bounds")
        return self.__data[index]
    def enqueue(self, value):
        if(self.isFull()):
            raise Exception("Cannot enqueue because the queue is full.")
        self.__data[self.__length] = value
        self.__length += 1
    def dequeue(self):
        if(self.isEmpty()):
            raise Exception("Cannot dequeue an empty queue")
        self.__data = self.__data[1:self.__length]
        self.__length -= 1
