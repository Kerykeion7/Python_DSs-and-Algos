import unittest
from LinkedLists import DoublyLinkedList as DblLlstClass

class Test_test_DoublyLinkedList(unittest.TestCase):
    def test_Not_None(self):
        lst = DblLlstClass.DoublyLinkedList()
        self.assertFalse(lst is None)

if __name__ == '__main__':
    unittest.main()
