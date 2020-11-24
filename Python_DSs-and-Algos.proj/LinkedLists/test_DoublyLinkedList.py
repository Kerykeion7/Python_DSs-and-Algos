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

    def test_getting(self):
        lst = self.__setUpMainLinkedList()
        self.assertTrue(lst.get_front() == 1
                        and lst.get_back() == 10
                        and lst.get_at(1) == 2
                        and lst.get_at_from_end(1) == 9)

    def test_removing(self):
        lst = self.__setUpMainLinkedList()
        self.assertTrue(lst.pop_back() == 10
                        and lst.pop_front() == 1
                        and lst.get_length() == 6)
        self.assertEquals(lst.get_at(4), 7)
        lst.remove_at(4)
        self.assertTrue(lst.get_at(4) != 7 
                        and lst.get_at(4) == 9 
                        and lst.get_at_from_end(0) == lst.get_at(4))
        self.assertEquals(lst.get_at(1), 3)
        lst.remove(3)
        self.assertNotEquals(lst.get_at(1), 3)
        

    def test_reversing(self):
        lst = self.__setUpMainLinkedList()
        lst.insert_at(4, 3)
        lst.insert_at(8, 7)
        counter = 1
        for i in range(lst.get_length() - 1):
            self.assertEquals(counter, lst.get_at(i))
            counter += 1
        lst.reverse()
        counter = 1
        for i in range(lst.get_length() - 1):
            self.assertEquals(counter, lst.get_at_from_end(i))
            counter += 1

if __name__ == '__main__':
    unittest.main()
