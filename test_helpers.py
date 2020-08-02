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

    def test_get_postfootnotes_without_prefootnotes(self):
        sample_text = "Here is one [^1] and two [^2] \n\n [^1]: hello"
        expected = ["1"]
        actual = h.getAllPostFootnotes(sample_text)
        error_message = f"Should be the following list: {expected} but got: {actual}"
        self.assertEqual(expected, actual, error_message)
    
    def test_get_multiple_postfootnotes(self):
        sample_text = "Hola mundo \n\n [^first]: hey there \n\n [^2]: hi"
        expected = ["first", "2"]
        actual = h.getAllPostFootnotes(sample_text)
        error_message = f"Should be the following list: {expected} but got: {actual}"
        self.assertEqual(expected, actual, error_message)   
        
    def test_has_no_duplicates(self):
        
        # Expect the following test to fail
        
        sample_list = ["1", "1"]
        with self.assertRaises(AssertionError) as cm: # cm probably stands for Context Manager
            h.ensureAllUnique(sample_list)
        expected_message = h.ERROR_MESSAGE_NO_DUPLICATES
        actual_message = cm.exception.args[0]
        self.assertEqual(expected_message, actual_message)
        
        # Expect the following test to pass
        
        sample_list_2 = ["1", "2"]
        try:
            h.ensureAllUnique(sample_list_2)
        except:
            self.fail("Shouldn't have an Exception")
            
    def test_prefootnotes_have_counterpart_in_postfootnotes(self):
        
        expected_message = h.ERROR_MESSAGE_SHOULD_HAVE_COUNTERPART
        
        # Expect the following test to fail
        
        list_of_pre = ["1"]
        list_of_postfootnotes = ["2"]
        with self.assertRaises(AssertionError) as cm:
            h.ensureAllPreHasCounterpartAmongPostFootnotes(list_of_pre, list_of_postfootnotes)
        actual_message = cm.exception.args[0]
        self.assertEqual(expected_message, actual_message)
        
        # Expect the following test to fail
        
        list2_of_pre = ["2", "1", "4"]
        list2_of_post = ["1", "2", "4"] # post is short for Post Footnotes, as you might have guessed
        with self.assertRaises(AssertionError) as cm2:
            h.ensureAllPreHasCounterpartAmongPostFootnotes(list2_of_pre, list2_of_post)
        actual_message = cm2.exception.args[0]
        self.assertEqual(expected_message, actual_message)
        
        # Expect the following test to pass
        list3_of_post = ["2", "1", "4"]
        try:
            # note that we compare list *two* with list *three*
            h.ensureAllPreHasCounterpartAmongPostFootnotes(list2_of_pre, list3_of_post)
        except:
            self.fail("Shouldn't have an Exception")
    
    def test_map_of_replacements_is_accurate(self):
        fn = ["first", "second"]
        expected = {
            "first": "1",
            "second": "2" 
        }
        actual = h.mapFootnotesToNumbers(fn)
        
        self.assertEqual(expected, actual)
        
        # just out of curiosity
        fn2 = []
        expected2 = {}
        actual2 = h.mapFootnotesToNumbers(fn2)
        self.assertEqual(expected2, actual2)
        
    def test_replace(self):
        sample_text = "Here is one [^alpha] and two [^beta] \n\n [^alpha]: hello \n\n [^beta]: world"
        sample_map = {
            "alpha": "1",
            "beta": "2" 
        }
        
        expected = "Here is one [^1] and two [^2] \n\n [^1]: hello \n\n [^2]: world"
        actual = h.replaceFootnotesWithNumbers(sample_text, sample_map)
        
        self.assertEqual(expected, actual)
        
    def test_build_footnote(self):
        fn = "foo"
        expected = "[^foo]"
        actual = h.buildFootnote(fn)
        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()