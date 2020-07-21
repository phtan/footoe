import unittest # Targeting Python 3
import footoe.helpers as h

class TestHelpers(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(sum([7, 7, 7, 7, 7, 7]), 42, "Should be 42")
        
    def test_get_prefootnotes(self):
        sample_text = "Here is one [^1] and another [^another]"
        expected = ["1", "another"]
        actual = h.getAllPreFootnotes(sample_text)
        error_message = f"Should be a list {expected}"
        self.assertEqual(expected, actual, error_message)
        
    def test_get_prefootnotes_without_postfootnotes(self):
        sample_text = "Here is one [^1] and two [^2] \n\n [^1]: hello"
        expected = ["1", "2"]
        actual = h.getAllPreFootnotes(sample_text)
        error_message = f"Should be a list {expected}"
        self.assertEqual(expected, actual, error_message)
        
    def test_has_no_duplicates(self):
        sample_list = ["1", "1"]
        with self.assertRaises(AssertionError) as cm: # cm probably stands for Context Manager
            h.ensureAllUnique(sample_list)
        expected_message = h.ERROR_MESSAGE_NO_DUPLICATES
        actual_message = cm.exception.args[0]
        self.assertEqual(expected_message, actual_message)
        
        sample_list_2 = ["1", "2"]
        try:
            h.ensureAllUnique(sample_list_2)
        except:
            self.fail("Shouldn't have an Exception")
            
if __name__ == "__main__":
    unittest.main()