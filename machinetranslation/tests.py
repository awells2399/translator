import unittest
from translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):
    """
    test cases
    """

    def test_no_input_english_to_french(self):
        """
        Test empty input from function
        """
        result = english_to_french('')
        self.assertEqual(result, None)

    def test_no_input_french_to_english(self):
        """
        Test empty input from function
        """
        result = french_to_english("")
        self.assertEqual(result, None)

    def test_english_to_french(self):
        """
        Test to translate input from english to french
        """
        response = english_to_french('Hello')
        expected = "Bonjour"
        self.assertEqual(response, expected)

    def test_list_fraction(self):
        """
        Test to translate input from french to english
        """
        response = french_to_english('Bonjour')
        expected = "Hello"
        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
