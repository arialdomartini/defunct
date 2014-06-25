import unittest

class TestDummy(unittest.TestCase):

    def test_pass(self):
        from defunct import defunct
        result = defunct.run()

        self.assertEqual(result, 'ok')
