"""test cases for translator"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Class to test the function english_to_french
    """
    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertEqual(english_to_french(None),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Class to test the function french_to_english
    """
    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertEqual(french_to_english(None),"")
        self.assertNotEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
