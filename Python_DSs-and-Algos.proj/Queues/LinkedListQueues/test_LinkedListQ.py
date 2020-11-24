from Queues.LinkedListQueues import LinkedListQ as qClass
import unittest

class Test_test_LinkedListQ(unittest.TestCase):
    def __setUpMainTestQ(self):
        q = qClass.LinkedListQ()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(8)
        q.enqueue(9)
        q.enqueue(10)
        return q

    def test_Is_Not_None(self):
        q = qClass.LinkedListQ()
        self.assertFalse(q is None)

    def test_Count_Equals_Eight(self):
        q = self.__setUpMainTestQ()
        self.assertEqual(8, q.getSize())

    def test_dequeuing_and_enqueuing(self):
        q = self.__setUpMainTestQ()
        self.assertTrue(q.dequeue() == 1
                        and q.dequeue() == 3
                        and q.getSize() == 6)

if __name__ == '__main__':
    unittest.main()
