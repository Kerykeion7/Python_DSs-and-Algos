import unittest
from HashTables import HashTable as hTableClass

class Test_test_HashTable(unittest.TestCase):
    def __setupMainTable(self):
        table = hTableClass.HashTable()
        table.add("TestKeyOne", 1)
        table.add("TestKeyTwo", 2)
        table.add("TestKeyThree", 3)
        table.add("TestKeyFour", 4)
        table.add("TestKeyFive", 5)
        table.add("TestKeySix", 6)
        table.add("TestKeySeven", 7)
        return table

    def test_Not_None(self):
        table = hTableClass.HashTable()
        self.assertIsNotNone(table)

    def test_Hash_Always_Returns_Same_Value(self):
        table = hTableClass.HashTable()
        testOneA = table.key_hash("TestOne")
        testOneB = table.key_hash("TestOne")
        self.assertEqual(testOneA, testOneB)
        testTwoA = table.key_hash("TestTwo")
        testTwoB = table.key_hash("TestTwo")
        self.assertEqual(testTwoA, testTwoB)
        testThreeA = table.key_hash("TestThree")
        testThreeB = table.key_hash("TestThree")
        self.assertEqual(testThreeA, testThreeB)

    def test_key_hash_Raises_Error_On_Invalid_Argument(self):
        table = hTableClass.HashTable()
        self.assertRaises(ValueError, table.key_hash, 0)
        self.assertRaises(ValueError, table.key_hash, "")

    def test_Add_First_Equals_Get_At_Hashed_Index(self):
        table = hTableClass.HashTable()
        hashed = table.key_hash("TestKeyOne")
        table.add("TestKeyOne", "TestValueOne")
        self.assertEqual(table.getAt(hashed), ("TestKeyOne", "TestValueOne"))

    def test_GetAt_Raises_IndexError(self):
        table = hTableClass.HashTable()
        table.add("TestKeyOne", "TestValueOne")
        self.assertRaises(IndexError, table.getAt, -5)
        self.assertRaises(IndexError, table.getAt, table.capacity())

    def test_resize(self):
        table = self.__setupMainTable()
        self.assertTrue(table.length() == 7)
        self.assertEqual(table.capacity(), 20)

    def test_getValue(self):
        table = self.__setupMainTable()
        self.assertEqual(table.getValue("TestKeyOne"), 1)
        self.assertEqual(table.getValue("TestKeyTwo"), 2)
        self.assertEqual(table.getValue("TestKeyThree"), 3)
        self.assertEqual(table.getValue("TestKeyFour"), 4)
        self.assertEqual(table.getValue("TestKeyFive"), 5)
        self.assertEqual(table.getValue("TestKeySix"), 6)
        self.assertEqual(table.getValue("TestKeySeven"), 7)
        self.assertNotEqual(table.getValue("TestKeyFour"), 8)
        self.assertRaises(KeyError, table.getValue, "FakeTest")

    def test_Override_Existing_Key(self):
        table = self.__setupMainTable()
        self.assertTrue(table.length() == 7)
        table.add("TestKeySix", "SixOverridden")
        self.assertTrue(table.length() == 7)
        table.add("TestKeyEight", 8)
        self.assertTrue(table.length() == 8)
        self.assertEqual(table.getValue("TestKeySix"), "SixOverridden")
        self.assertNotEqual(table.getValue("TestKeySix"), 6)
        self.assertEqual(table.getValue("TestKeyEight"), 8)

    def test_Exists(self):
        table = self.__setupMainTable()
        self.assertTrue(table.exists("TestKeyOne"))
        self.assertFalse(table.exists("TestKeyEight"))

    def test_Remove(self):
        table = self.__setupMainTable()
        self.assertTrue(table.exists("TestKeyTwo"))
        self.assertTrue(table.length() == 7)
        table.remove("TestKeyTwo")
        self.assertTrue(table.length() == 6)
        self.assertFalse(table.exists("TestKeyTwo"))
        self.assertRaises(KeyError, table.remove, "FakeTest")

    def test_resize_2(self):
        table = self.__setupMainTable()
        table.add("TestKeyEight", 8)
        table.add("TestKeyNine", 9)
        table.add("TestKeyTen", 10)
        table.add("TestKeyEleven", 11)
        table.add("TestKeyTwelve", 12)
        table.add("TestKeyThirteen", 13)
        table.add("TestKeyFourteen", 14)
        self.assertEqual(table.capacity(), 40)
        self.assertEqual(table.length(), 14)
        tableKeySet = set()
        counter = 0
        for i in range(table.capacity()):
            if table.getAt(i) is not None:
                tableKeySet.add(table.getAt(i)[0])
                counter += 1
        self.assertEqual(len(tableKeySet), table.length())
        self.assertEqual(counter, table.length())

if __name__ == '__main__':
    unittest.main()
