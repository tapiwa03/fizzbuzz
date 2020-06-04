import sys
import unittest
from unittest.mock import patch

from fizzbuzz.app import run, fizz_buzz, convert_to_int


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_returns_correct_list(self):
        """
        Test that fizzbuzz list has correct values for multiples
        """
        fizzbuzz = fizz_buzz(1, 15)
        self.assertEqual(fizzbuzz[0], 1, "List did not start with the number 1")
        self.assertEqual(
            fizzbuzz[-1],
            "FizzBuzz",
            "Multiple of both 3 and 5 (15) did not print FizzBuzz",
        )
        self.assertEqual(fizzbuzz[2], "Fizz", "Multiple of 3 (3) did not print Fizz")
        self.assertEqual(fizzbuzz[4], "Buzz", "Multiple of 5 (5) did not print Buzz")

    def test_convert_to_int_returns_defaults(self):
        """
        Test that converting the numbers returns a [1, 100] if empty list is passed
        """
        integer_list = convert_to_int([])[0]
        print(integer_list)
        self.assertEqual(integer_list[0], 1, "List did not start with the number 1")
        self.assertEqual(integer_list[1], 100, "List did not end with the number 100")

    def test_convert_to_int_returns_error_for_non_integers(self):
        """
        Test that converting the numbers returns a [1, 100] if empty list is passed
        """
        integer_list = convert_to_int(["something"])
        self.assertEqual(
            integer_list[1],
            "Please enter integers only",
            "Convert to int did not return an error for non int value",
        )

    def test_convert_to_int_returns_error_for_more_than_2_args(self):
        """
        Test that more than 2 args will result in error
        """
        integer_list = convert_to_int([1, 2, 3])
        self.assertEqual(
            integer_list[1],
            "You cannot enter more than 2 arguments",
            "Convert to int did not return an error for more than 2 args",
        )

    def test_convert_to_int_returns_error_for_zero_as_an_arg(self):
        """
        Test that zero is not accepted as an arg
        """
        integer_list = convert_to_int([1, 0])
        self.assertEqual(
            integer_list[1],
            "When entering integers ensure they are greater than 0",
            "Convert int did not throw an error when zero was passed",
        )

    def test_convert_to_int_returns_1_as_min_value_when_single_arg_is_provided(self):
        """
        Test that 1 is returned as the min value if one argument is passed
        """
        integer_list = convert_to_int([80])[0]
        self.assertEqual(
            integer_list[0],
            1,
            "Convert to int did not return a minimum value when provided with a single argument",
        )

    def test_run_function_accepts_args(self):
        """
        Test that the run function runs and prints
        """
        testargs = ["main.py", "1", "3"]
        with patch.object(sys, "argv", testargs):
            self.assertEqual(
                run(), "Success", "The run function did not go all the way through",
            )

    def test_run_function_returns_errors_when_invalid_args_passed(self):
        """
        Test that the run function runs and prints
        """
        testargs = ["main.py", 1, 2, 3, 4]
        with patch.object(sys, "argv", testargs):
            with self.assertRaises(Exception):
                run()


if __name__ == "__main__":
    unittest.main()
