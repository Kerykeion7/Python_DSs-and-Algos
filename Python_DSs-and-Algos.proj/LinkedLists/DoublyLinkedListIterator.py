class DoublyLinkedListIterator:
    def __init__(self, Head):
        self.__current = Head
    def __next__(self):
        if(self.__current is None):
            raise StopIteration
        current = self.__current
        self.__current = self.__current.Next
        return current
