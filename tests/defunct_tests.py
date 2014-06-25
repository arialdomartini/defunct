import unittest
from defunct import defunct

class DefunctTests(unittest.TestCase):

    def test_that_an_empty_string_has_no_tokens(self):
        result = defunct.tokenize('')

        self.assertEqual(result, [])


    def test_that_an_s_expression_is_tokenized(self):
        result = defunct.tokenize("(foo bar 3)")

        for e in ['(', 'foo', 'bar', '3', ')']:
            self.assertIn(e, result)
