import unittest
from defunct import defunct

class DefunctTests(unittest.TestCase):

    def test_that_an_empty_string_has_no_tokens(self):
        
        result = defunct.tokenize('')

        self.assertEqual(result, [])
