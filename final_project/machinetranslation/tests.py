import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        if english_to_french is not None:
            self.assertEqual(english_to_french('Hello'),'Bonjour')
            self.assertNotEqual(english_to_french("yellow"),"robe")

    def test_french_to_english(self):
        if french_to_english is not None:
            self.assertEqual(french_to_english('Bonjour'),'Hello')
            self.assertNotEqual(french_to_english("robe"),"yellow")


if __name__ == '__main__':
    unittest.main()
