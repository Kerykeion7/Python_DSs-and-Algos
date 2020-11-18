from Arrays import DynamicArrayIterator

class DynamicArray:
    Count = 0
    __minCapacity = 4
    __capacity = 0
    __items = []

    def __init__(self, capacity = 4):
        self.__capacity = capacity
        self.__items = ["NULL"]*self.__capacity

    def push(self, item):
        self.__resize()
        self.__items[self.Count] = item
        self.Count += 1

    def get_at(self, index):
        self.__raise_if_index_out_of_bounds(index)
        return self.__items[index]

    def is_empty(self):
        return self.Count == 0

    def capacity(self):
        return self.__capacity

    def size(self):
        return self.Count

    def pop(self):
        self.__raise_if_index_out_of_bounds(self.Count - 1)
        popped = self.__items[self.Count - 1]
        self.__items[self.Count - 1] = "NULL"
        self.Count -= 1
        self.__resize()
        return popped

    def insert_at(self, item, index):
        self.__raise_if_index_out_of_bounds(index)
        self.__resize()
        self.__items = self.__items[0:index] + [item] + self.__items[index:self.Count]
        self.Count += 1

    def prepend(self, item):
        self.insert_at(item, 0)

    def index_of(self, item):
        for i in range(self.Count):
            if self.__items[i] == item:
                return i

        return -1

    def remove_at(self, index):
        self.__raise_if_index_out_of_bounds(index)
        self.__resize()
        self.__items = self.__items[0:index] + self.__items[index + 1:self.Count]
        self.Count -= 1

    def remove(self, item):
        index = 0
        while index < self.Count:
            if self.__items[index] == item:
                self.remove_at(index)
                index -= 1
                continue
            index += 1
            

    def __resize(self):
        if self.Count == self.__capacity:
            self.__capacity *= 2
            self.__allocate()
        
        if self.Count <= int(self.__capacity / 4):
            if (int(self.__capacity / 2)) >= self.__minCapacity:
                self.__capacity = int(self.__capacity / 2)
                self.__allocate()

    def __allocate(self):
        new_items = ["NULL"]*self.__capacity
        new_items = self.__items[0:len(self.__items)] + new_items[len(self.__items):self.__capacity]
        self.__items = new_items

    def __raise_if_index_out_of_bounds(self, index):
        if index > self.Count - 1 or index < 0:
            raise IndexError("Index out of bounds mate")

    def __iter__(self):
        return DynamicArrayIterator(self.__items, self.Count)


