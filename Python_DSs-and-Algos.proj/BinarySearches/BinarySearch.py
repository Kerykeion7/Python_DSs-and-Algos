class BinarySearch:
    def __binary_search(self, array:list, left, right, searchVal:int) -> int:
        index = (int)((right - left) / 2)
        if index <= left: index += left
        val = array[index]

        if val > searchVal: return self.__binary_search(array, left, index, searchVal)
        if val < searchVal: return self.__binary_search(array, index, right, searchVal)
        if val == searchVal: return index

        return -1;

    def binarySearch(self, array:list, searchVal:int) -> int:
        if not isinstance(array, list):
            raise TypeError
        if not isinstance(searchVal, int):
            raise TypeError
        if array.count(searchVal) == 0:
            raise ValueError
        array.sort()
        return self.__binary_search(array, 0, len(array), searchVal)
