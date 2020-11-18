from Queues.LinkedListQueues import LinkedListQ as qClass
import unittest

class Test_test_LinkedListQ(unittest.TestCase):
    def test_A(self):
        q = qClass.LinkedListQ()
        self.assertFalse(q is None)

if __name__ == '__main__':
    unittest.main()
