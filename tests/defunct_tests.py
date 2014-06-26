import unittest
from defunct import defunct
import sure

class DefunctTests(unittest.TestCase):

    def test_that_an_empty_string_has_no_tokens(self):
        result = defunct.tokenize('')

        result.should.equal([])


    def test_that_an_s_expression_is_tokenized(self):
        result = defunct.tokenize("(foo bar 3)")
        
        result.should.equal(['(', 'foo', 'bar', '3', ')'])
