from LinkedLists import DoublyLinkedListIterator
from LinkedLists import DoublyLinkedNode

class DoublyLinkedList():
    __length = 0
    Head = None
    Tail = None

    def __iter__(self):
        return DoublyLinkedListIterator(self.Head)

    def __first_push(self, node):
        if self.Head is None:
            self.Head = node
            self.Tail = node
            return True
        return False
    
    def __get_constant_time(self, index):
        if index == 0:
            return self.get_front()
        if index == self.__length - 1:
            return self.get_back()
        return None

    def __get_linear_time(self, loopCount):
        node = self.Head
        for i in range(loopCount):
            node = node.Next
        return node.Value

    def __throw_get_at_if_necessary(self, index):
        self.__throw_if_empty()
        self.__throw_int_exception_if_necessary(index)
        if index < 0 or index > self.__length - 1:
            raise Exception("Index out of bounds.")

    def __throw_int_exception_if_necessary(self, index):
        if isinstance(index, int) == False:
            raise Exception("Given index is not of type integer.")
    
    def __throw_if_empty(self):
        if self.is_empty(): raise Exception("The list is empty.")

    def __get_at_helper(self, loopCount):
        self.__throw_get_at_if_necessary(loopCount)
        value = self.__get_constant_time(loopCount)
        if value is not None:
            return value
        return self.__get_linear_time(loopCount)

    def get_length(self):
        return self.__length
    
    def is_empty(self):
        return self.__length == 0

    def push_front(self, value):
        node = DoublyLinkedNode(value)
        if self.__first_push(node) == False:
            node.Next = self.Head
            self.Head.Previous = node
            self.Head = node
        self.__length += 1

    def push_back(self, value):
        node = DoublyLinkedNode(value)
        if self.__first_push(node) == False:
            node.Previous = self.Tail
            self.Tail.Next = node
            self.Tail = node
        self.__length += 1

    def insert_at(self, value, index):
        self.__throw_int_exception_if_necessary(index)
        if index < 0 or index > self.__length + 1:
            raise Exception("Index out of bounds.")
        if index == 0:
            self.push_front(value)
            return
        if index == self.__length:
            self.push_back(value)
            return
        node = DoublyLinkedNode(value)
        current = self.Head
        for n in range(index - 1):
            current = current.Next
        currentNext = current.Next
        node.Next = currentNext 
        currentNext.Previous = node 
        current.Next = node
        node.Previous = current
        self.__length += 1
    
    def reverse(self):
        if self.is_empty(): raise Exception("The list is empty.")
        prev = None
        current = self.Head
        nxt = current.Next
        while nxt is not None:
            prev = current
            current = nxt
            nxt = current.Next
            current.Previous = nxt
            current.Next = prev
        self.Tail = self.Head
        self.Tail.Previous = self.Tail.Next
        self.Tail.Next = None
        self.Head = current
        self.Head.Previous = None

    def get_front(self):
        if self.is_empty(): raise Exception("The list is empty.")
        return self.Head.Value
    
    def get_back(self):
        if self.is_empty(): raise Exception("The list is empty.")
        return self.Tail.Value

    def get_at(self, index):
        return self.__get_at_helper(index)

    def get_at_from_end(self, index):
        return self.__get_at_helper(self.__length - 1 - index)

    def pop_front(self):
        self.__throw_if_empty()
        newHead = self.Head.Next
        oldVal = self.Head.Value
        self.Head = newHead
        newHead.Previous = None
        self.__length -= 1
        return oldVal

    def pop_back(self):
        self.__throw_if_empty()
        newTail = self.Tail.Previous
        oldVal = self.Tail.Value
        self.Tail = newTail
        newTail.Next = None
        self.__length -= 1
        return oldVal

    def remove_at(self, index):
        self.__throw_if_empty()
        self.__throw_int_exception_if_necessary(index)
        if index < 0 or index > self.__length - 1:
            raise Exception("Index out of bounds.")
        if index == 0:
            self.pop_front()
            return
        if index == (self.__length - 1):
            self.pop_back()
            return
        node = self.Head
        for i in range(index):
            node = node.Next
        nxt = node.Next
        prev = node.Previous
        prev.Next = nxt
        nxt.Previous = prev  
        self.__length -= 1     

    def remove(self, value):
        index = 0
        for item in self:
            if item.Value == value:
                self.remove_at(index)
                return
            index += 1
        print("No item found with value: " + str(value))
