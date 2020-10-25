import unittest

#from ../../functions.test_data import test_data

from modules.woodside.functions.test_data import test_data


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(test_data(), 'yes')


if __name__ == '__main__':
    unittest.main()