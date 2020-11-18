import unittest
from Arrays import DynamicArray as DynamicArrayClass

class Test_test_DynamicArray(unittest.TestCase):
    def test_Not_None(self):
        array = DynamicArrayClass.DynamicArray()
        self.assertFalse(array is None)

if __name__ == '__main__':
    unittest.main()
