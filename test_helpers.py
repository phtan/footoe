import unittest # Targeting Python 3
import footoe.helpers as h

class TestHelpers(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(sum([7, 7, 7, 7, 7, 7]), 42, "Should be 42")
        
    def test_get_pre(self):
        sample_text = "Here is one [^1] and another [^another]"
        expected = ["1", "another"]
        actual = h.getAllPreFootnotes(sample_text)
        error_message = f"Should be a list {expected}"
        self.assertEqual(expected, actual, error_message)
        
    def test_get_pre_without_postfootnotes(self):
        sample_text = "Here is one [^1] and two [^2] \n\n [^1]: hello"
        expected = ["1", "2"]
        actual = h.getAllPreFootnotes(sample_text)
        error_message = f"Should be a list {expected}"
        self.assertEqual(expected, actual, error_message)
        
if __name__ == "__main__":
    unittest.main()