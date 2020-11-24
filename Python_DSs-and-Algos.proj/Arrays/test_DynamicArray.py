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

    def test_Capacity_Equals_MinOrGiven_Capacity(self):
        array1 = DynamicArrayClass.DynamicArray()
        self.assertEquals(4, array1.capacity())
        array2 = DynamicArrayClass.DynamicArray(2)
        self.assertEquals(4, array2.capacity())
        array3 = DynamicArrayClass.DynamicArray(100)
        self.assertEquals(100, array3.capacity())

    def test_IsEmpty(self):
        array1 = DynamicArrayClass.DynamicArray()
        self.assertTrue(array1.is_empty())
        array1.push(1)
        self.assertFalse(array1.is_empty())

    def test_Adding(self):
        array = self.__setUpMainArray()
        self.assertTrue(array.Count == 8 and array.capacity() == 8)
        array.push(10)
        self.assertTrue(array.Count == 9 and array.capacity() == 16)
        array.prepend("zero")
        array.insert_at("four", 3)
        self.assertTrue(array.Count == 11)
        self.assertRaises(IndexError, array.get_at, array.Count)
        self.assertRaises(IndexError, array.get_at, -1)
        self.assertTrue(array.get_at(array.Count - 1) == 10)
        self.assertTrue(array.get_at(3) == "four")
        self.assertTrue(array.get_at(0) == "zero")

    def test_Removing(self):
        array = self.__setUpMainArray()
        self.assertTrue(array.size() == 8 and array.capacity() == 8)
        array.push(10)
        self.assertTrue(array.size() == 9 and array.capacity() == 16)
        self.assertTrue(array.pop() == 10
                        and array.pop() == "Nine"
                        and array.pop() == "Eight"
                        and array.pop() == 7
                        and array.pop() == "Six")
        self.assertTrue(array.size() == 4 and array.capacity() == 8)
        self.assertTrue(2 == array.index_of(3))
        array.remove_at(2)
        self.assertTrue(-1 == array.index_of(3))
        self.assertEqual(2, array.index_of(5))
        self.assertTrue(3 == array.size() and array.capacity() == 8)
        array.insert_at(5, 2)
        self.assertTrue(4 == array.Count and array.capacity() == 8)
        array.push(5)
        array.prepend(5)
        self.assertTrue(array.Count == 6 and array.capacity() == 8)
        array.remove(5)
        self.assertTrue(array.Count == 2 and array.capacity() == 8)
        array.pop()
        self.assertTrue(array.Count == 1 and array.capacity() == 8)



if __name__ == '__main__':
    unittest.main()
