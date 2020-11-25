class BinarySearch:
    def __binary_search(self, array:list, searchVal:int) -> int:
        mid = (int)(len(array) / 2)
        val = array[mid]
        returnValue = 0
        if len(array) > 0:
            if val > searchVal:
                return self.__binary_search(array[0:mid], searchVal)
            if val < searchVal:
                return self.__binary_search(array[mid:len(array)], searchVal)
            return val


    def binarySearch(self, array:list, searchVal:int) -> int:
        if not isinstance(array, list):
            raise TypeError
        if not isinstance(searchVal, int):
            raise TypeError
        if array.count(searchVal) == 0:
            raise ValueError
        array.sort()
        return self.__binary_search(array, searchVal)
