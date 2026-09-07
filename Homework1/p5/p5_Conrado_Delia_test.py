import unittest

from p5_Conrado_Delia import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher(self):
        result = caesar_cipher("Hello World", 3)
        self.assertEqual(result, "Khoor Zruog")

    def test_caesar_decipher(self):
        result = caesar_decipher("Khoor Zruog", 3)
        self.assertEqual(result, "Hello World")

    def test_preserve_spaces_and_punctuation(self):
        result = caesar_cipher("Hello, World!", 3)
        self.assertEqual(result, "Khoor, Zruog!")

    def test_wrap_around(self):
        result = caesar_cipher("XYZ", 3)
        self.assertEqual(result, "ABC")

    def test_letter_frequency(self):
        result = letter_frequency("Hello World!")

        self.assertEqual(result["h"], 1)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["l"], 3)
        self.assertEqual(result["o"], 2)
        self.assertEqual(result["w"], 1)
        self.assertEqual(result["r"], 1)
        self.assertEqual(result["d"], 1)

    def test_letter_frequency_ignores_case(self):
        result = letter_frequency("AaBbC")

        self.assertEqual(result["a"], 2)
        self.assertEqual(result["b"], 2)
        self.assertEqual(result["c"], 1)


if __name__ == "__main__":
    unittest.main()