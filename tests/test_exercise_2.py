import unittest

from python_exercises.src.exercise_2 import sum_arrays, factorial, multiply_numbers, multiply_array_by_number


class TestMathOperations(unittest.TestCase):

    def test_sum_arrays(self):
        self.assertEqual(sum_arrays([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_arrays([9, 9], [1]), [1, 0, 0])
        self.assertEqual(sum_arrays([0], [0]), [0])

    def test_factorial(self):
        self.assertEqual(factorial(0), [1])
        self.assertEqual(factorial(1), [1])
        self.assertEqual(factorial(5), [1, 2, 0])  # 5! = 120
        self.assertEqual(factorial(10), [3, 6, 2, 8, 8, 0, 0])  # 10! = 3628800

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(0, 123), [0])
        self.assertEqual(multiply_numbers(123, 0), [0])
        self.assertEqual(multiply_numbers(3, 4), [1, 2])  # 3 * 4 = 12
        self.assertEqual(multiply_numbers(-3, 4), ["-", 1, 2])  # -3 * 4 = -12
        self.assertEqual(multiply_numbers(-3, -4), [1, 2])  # -3 * -4 = 12

    def test_multiply_array_by_number(self):
        self.assertEqual(multiply_array_by_number([1, 2], 3), [3, 6])  # 12 * 3 = 36
        self.assertEqual(multiply_array_by_number([1, 0, 0], 2), [2, 0, 0])  # 100 * 2 = 200
        self.assertEqual(multiply_array_by_number([0], 10), [0])

if __name__ == "__main__":
    unittest.main()