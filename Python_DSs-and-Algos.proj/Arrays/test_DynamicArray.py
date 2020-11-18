import unittest
from Arrays import DynamicArray as DynamicArrayClass

class Test_test_DynamicArray(unittest.TestCase):
    def __setUpMainArray(self):
        array = DynamicArrayClass.DynamicArray()
        array.push(1)
        array.push(2)
        array.push(3)
        array.push(5)
        array.push("Six")
        array.push(7)
        array.push("Eight")
        array.push("Nine")
        return array

    def test_Not_None(self):
        array = self.__setUpMainArray()
        self.assertFalse(array is None)

    def test_Count_Equals_Eight(self):
        array = self.__setUpMainArray()
        self.assertEquals(8, array.Count)

if __name__ == '__main__':
    unittest.main()
