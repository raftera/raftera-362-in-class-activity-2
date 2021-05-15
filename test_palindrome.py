import unittest
import pytest
import palindrome



class TestCase(unittest.TestCase):

    def test_palindrome(self):
        result = palindrome.palindrome("civic")
        self.assertEqual(1, result)
    def test_palindrome2(self):
        result = palindrome.palindrome("racecar")
        self.assertEqual(1, result)
    def test_palindrome3(self):
        result = palindrome.palindrome("25")
        self.assertEqual(1, result)
    def test_palindrome4(self):
        result = palindrome.palindrome(25)
        self.assertEqual(0, result)
    def test_palindrome5(self):
        result = palindrome.palindrome(252)
        self.assertEqual(1, result)
    def test_palindrome6(self):
        result = palindrome.palindrome("252")
        self.assertEqual(1, result)
   
if __name__ == '__main__':

    unittest.main()
    
