import unittest
from LinkedLists import DoublyLinkedList as DblLlstClass

class Test_test_DoublyLinkedList(unittest.TestCase):
    def __setUpMainLinkedList(self):
        lst = DblLlstClass.DoublyLinkedList()
        lst.push_back(1)
        lst.push_back(2)
        lst.push_back(3)
        lst.push_back(5)
        lst.push_back(6)
        lst.push_back(7)
        lst.push_back(9)
        lst.push_back(10)
        return lst

    def test_Not_None(self):
        lst = self.__setUpMainLinkedList()
        self.assertFalse(lst is None)

    def test_Count_Equals_Eight(self):
        lst = self.__setUpMainLinkedList()
        self.assertEqual(8, lst.get_length())

if __name__ == '__main__':
    unittest.main()
