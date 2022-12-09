import unittest
from unittest.mock import patch
from phonebook_item import PhonebookItem


# test phonebook_item.py
class TestPhonebookItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.contact_1 = PhonebookItem('John', 'Green', 123456789)
        self.contact_2 = PhonebookItem('Lisa', 'Gray', 987654321)

    def tearDown(self):
        pass

    def test__str__(self):
        self.assertEqual(self.contact_1.__str__(), "John Green - 123456789")
        self.assertEqual(self.contact_2.__str__(), "Lisa Gray - 987654321")


if __name__ == '__main__':
    unittest.main()
