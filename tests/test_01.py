import unittest


class TestCase01(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def test_something_else(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
