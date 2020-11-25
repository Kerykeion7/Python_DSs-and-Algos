import unittest
from BinarySearches import BinarySearch as BSclass

class Test_test_BinarySearch(unittest.TestCase):
    def test_A(self):
        srchr = BSclass.BinarySearch()
        arr = [10, 5, 7, 3, 15, 9, 32, 6]
        result = srchr.binarySearch(arr, 5)
        self.assertEquals(5, result)

    def test_B(self):
        srchr = BSclass.BinarySearch()
        arr = [150, 5, 7, 1394, 5, 61, 666, 1111, 88, 9, 111, 33, 4, 10, 12, 55, 34]
        result = srchr.binarySearch(arr, 150)
        self.assertEquals(150, result)

    def test_C(self):
        srchr = BSclass.BinarySearch()
        arr = [5, 1]
        result = srchr.binarySearch(arr, 1)
        self.assertEquals(1, result)

    def test_D(self):
        srchr = BSclass.BinarySearch()
        arr = [5]
        result = srchr.binarySearch(arr, 5)
        self.assertEquals(5, result)

    def test_E(self):
        srchr = BSclass.BinarySearch()
        arr = [5, 1]
        self.assertRaises(ValueError, srchr.binarySearch, arr, 3)


if __name__ == '__main__':
    unittest.main()
