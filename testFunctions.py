import unittest2
import functions

class TestClass(unittest2.TestCase):

    def test_add(self):
        result = functions.add(100, 5)
        self.assertEqual(result, 105)
        self.assertEqual(functions.add(100, 1), 101)

    def test_subtract(self):
        result = functions.subtract(100, 5)
        self.assertEqual(result, 95)

    def test_divide(self):
        self.assertEqual(functions.divide(100, 2), 50)

        with self.assertRaises(ValueError):
            functions.divide(100, 0)
    def test_multiply(self):
        self.assertEqual(functions.multuply(120, -3), -360)

if __name__ == "__main__":
    unittest2.main()