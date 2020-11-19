from Queues.ArrayQueues import ArrayQ as Qclass
import unittest

class Test_test_ArrayQ(unittest.TestCase):
    def __setUpMainArrayQ(self):
        q = Qclass.ArrayQ()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(6)
        return q

    def test_Q_Not_None(self):
        q = None
        self.assertTrue(q is None)
        q = Qclass.ArrayQ()
        self.assertFalse(q is None)

    def test_Q_Is_Empty(self):
        q = self.__setUpMainArrayQ()
        self.assertFalse(q is None)
        self.assertEqual(4, q.getSize())
        self.assertFalse(q.isEmpty())
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.isEmpty())

    def test_Q_Count_Equals_Four(self):
        q = self.__setUpMainArrayQ()
        self.assertFalse(q is None)
        self.assertEqual(4, q.getSize())

    def test_Q_Raises_Exception_On_Dequeuing_EmptyQ(self):
        q = Qclass.ArrayQ()
        self.assertFalse(q is None)
        self.assertTrue(q.isEmpty())
        with self.assertRaises(Exception) as context:
            q.dequeue()
        self.assertEqual("Cannot dequeue an empty queue", str(context.exception))

    def test_Q_Raises_Exception_On_Enqueuing_FullQ(self):
        q = self.__setUpMainArrayQ()
        self.assertFalse(q is None)
        q.enqueue("Test")
        q.enqueue("AnotherTest")
        self.assertTrue(q.isFull())
        with self.assertRaises(Exception) as context:
            q.enqueue(66)
        self.assertEqual("Cannot enqueue because the queue is full.", str(context.exception))

    def test_GetAt(self):
        q = self.__setUpMainArrayQ()
        self.assertEqual(6, q.getAt(3))
        self.assertRaises(IndexError, q.getAt, 4)
        self.assertRaises(IndexError, q.getAt, -1)

    def test_Dequeuing(self):
        q = self.__setUpMainArrayQ()
        self.assertFalse(q.getAt(0) is None)
        self.assertFalse(q.getAt(q.getSize() - 1) is None)
        self.assertEquals(q.getAt(0), 1)
        self.assertEquals(q.getAt(q.getSize() - 1), 6)
        q.dequeue()
        self.assertFalse(q.getAt(0) is 1)
        self.assertEqual(q.getAt(0), 3)

if __name__ == '__main__':
    unittest.main()
