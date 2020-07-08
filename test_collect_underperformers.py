import unittest
import underperformers

# Note: this test suite does not contain a complete set of test cases.

class TestCollectUnderperformers(unittest.TestCase):

    def test_low_threshold(self):
        """ Test collect_underperformers with a threshold for which there
        are no underperformers."""

        actual = underperformers.collect_underperformers([4, 5, 6], 1)
        expected = []
        self.assertEqual(actual, expected)


    def test_high_threshold(self):
        """ Test collect_underperformers with a threshold for which all items
        are underperformers."""










        
    def test_mutation(self):
        """ Confirm that collect_underperformers does not mutate the list it's given."""
        
        


        
        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
        
        