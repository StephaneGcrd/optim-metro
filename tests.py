import unittest
import station

class TestStringMethods(unittest.TestCase):

    def create_stations(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()