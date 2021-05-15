import unittest
import palindrome

class TestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(true, palindrome("civic"))
    def test_palindrome2(self):
        self.assertEqual(true, palindrome("racecar"))