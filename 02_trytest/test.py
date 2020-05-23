import main    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(main.increment(3), 4)


if __name__ == '__main__':
    unittest.main()