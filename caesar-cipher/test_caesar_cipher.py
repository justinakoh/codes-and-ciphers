# These are the test cases for the caesar-cypher
import unittest
import mock
from mock import patch
from caesar_cypher import main
from caesar_cypher import calc_spaces_to_shift_by, output_letter, encode_text

# Tests that check whether it is able to calculate the spaces which we need to shift the letters by
class test_spaces_to_shift_by(unittest.TestCase):
    def test_it_can_calculate_normal_difference(self):
        expected = 1
        actual = calc_spaces_to_shift_by("a", "b")
        self.assertEqual(actual, expected)

    # rename the test name to something more appropriate
    def test_it_can_calculate_a_full_rotation(self):
        expected = 25
        actual = calc_spaces_to_shift_by("b", "a")
        self.assertEqual(actual, expected)

    def test_it_returns_correct_value_when_going_to_beginning_of_alphabet(self):
        expected = 2
        actual = calc_spaces_to_shift_by("z", "b")
        self.assertEqual(actual, expected)


# Test that check whether the correct letters are outputted
class test_outputted_letters(unittest.TestCase):
    def test_it_can_output_the_correct_letters(self):
        expected = "b"
        actual = output_letter("a", 1)
        self.assertEqual(actual, expected)

    def test_correct_letter_is_outputted_when_cycle_is_made(self):
        expected = "a"
        actual = output_letter("z", 1)
        self.assertEqual(actual, expected)

    def test_it_does_not_encrypt_spaces(self):
        expected = " "
        actual = output_letter(" ", 1)
        print("Actual", actual)
        self.assertEqual(actual, expected)

    def test_it_encrypts_numbers(self):
        expected = "2"
        actual = output_letter("1", 1)
        self.assertEqual(actual, expected)

# #  9 should cycle back to 0 instead of going to the next letter.
#     def test_it_encrypts_numbers_when_a_cycle_is_preformed(self):
#         expected = "0"
#         actual = output_letter("9", 1)
#         self.assertEqual(actual, expected)


class test_encode_text(unittest.TestCase):
    def test_it_outputs_correct_text(self):
        expected = "bcde"
        actual = encode_text("abcd", 1)
        self.assertEqual(actual, expected)

    def test_it_outputs_correct_text_after_converting(self):
        expected = "abcd"
        first_conversion = encode_text("abcd", 1)
        actual = encode_text(first_conversion, -1)
        self.assertEqual(actual, expected)

    def test_it_does_not_encrypt_spaces_within_texts(self):
        expected = "b c d e"
        actual = encode_text("a b c d", 1)
        self.assertEqual(actual, expected)

    def test_it_does_not_encrypt_numbers_within_texts(self):
        expected = "2b3c4d"
        actual = encode_text("1a2b3c", 1)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
