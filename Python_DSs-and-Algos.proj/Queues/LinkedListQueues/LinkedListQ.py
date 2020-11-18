from Queues.LinkedListQueues import SinglyLinkedNode

class LinkedListQ():
    Head = None
    Tail = None
    __size = 0
    def __init__(self):
        pass
    
    def getSize(self):
        return self.__size;

    def isEmpty(self):
        return self.__size == 0

    def enqueue(self, value):
        node = SinglyLinkedNode(value)
        if self.isEmpty():
            self.Head = node
        else:
            self.Tail.Next = node
        self.Tail = node
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue an empty queue")
        oldVal = self.Head.Value
        self.Head = self.Head.Next
        self.__size -= 1
        return oldVal
