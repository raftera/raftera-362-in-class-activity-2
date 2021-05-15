import unittest
import wordcount

class TestCase(unittest.TestCase):
    def test_wordcount1(self):
        result = wordcount.wordcount("Should be four words")
        self.assertEqual(result, 4)
    def test_wordcount2(self):
        result = wordcount.wordcount("Two words")
        self.assertEqual(result, 2)
    def test_wordcount3(self):
        result = wordcount.wordcount("Oneword")
        self.assertEqual(result, 1)
    def test_wordcount4(self):
        result = wordcount.wordcount(fail)
        self.assertEqual(result, 3)
    def test_wordcount5(self):
        result = wordcount.wordcount(1234)
        self.assertEqual(result, 3)
    def test_wordcount6(self):
        result = wordcount.wordcount("M a n y w o r d s")
        self.assertEqual(result, 9)
if __name__ == '__main__':
    unittest.main()