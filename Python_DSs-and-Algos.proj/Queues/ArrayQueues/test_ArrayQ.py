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
        q = Qclass.ArrayQ()
        self.assertFalse(q is None)

    def test_Q_Count_Equals_Four(self):
        q = self.__setUpMainArrayQ()
        self.assertEqual(4, q.getSize())

if __name__ == '__main__':
    unittest.main()
