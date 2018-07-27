import unittest
import mycode


class Tester(unittest.TestCase):
    def test_sum_of_1_and_2(self):

        self.assertEqual(mycode.mysum(1, 2), 3)

    def test_sum_floats(self):
        self.assertEqual(mycode.mysum(1.00001, 0.99999), 2)

    def test_output_datatype(self):
        self.assertEqual(type(mycode.mysum(1, 1)), float)

if __name__ == '__main__':
    unittest.main()
