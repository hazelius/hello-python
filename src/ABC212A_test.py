import ABC212A
import unittest


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ABC212A.main(), 3)


if __name__ == '__main__':
    unittest.main()
