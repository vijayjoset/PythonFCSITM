
import unittest
import capitalize_text

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = capitalize_text.capitalize_t(text)
        self.assertEqual(result,'Python')
        
    def test_multiple_words(self):
        text = "my python"
        result = capitalize_text.capitalize_t(text)
        self.assertEqual(result,'My python')

if __name__ == '__main__':
    unittest.main()
