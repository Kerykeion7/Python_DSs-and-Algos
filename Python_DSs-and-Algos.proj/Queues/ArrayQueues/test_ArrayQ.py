from Queues.ArrayQueues import ArrayQ as Qclass
import unittest

class Test_test_ArrayQ(unittest.TestCase):
    def test_A(self):
        q = Qclass.ArrayQ()
        self.assertFalse(q is None)

if __name__ == '__main__':
    unittest.main()
