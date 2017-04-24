"""A full test suite for coalition."""

import unittest
import vcard


class TestVcardModule(unittest.TestCase):
    """Test the vcard reader, parsers, etc..."""

    def test_name_str(self):
        """Test the vcard.utility.Name class __str__ method."""
        test_name = vcard.utility.Name('John', 'Doe')
        test_str = """Name({'_middle': None, '_given': 'John',\
 '_prefix': None, '_nick': None, '_suffix': None, '_family': 'Doe'})"""
        self.assertEqual(str(test_name), test_str)

    def test_name_fields(self):
        """Test the vcard.utility.Name class fields."""
        test_name = vcard.utility.Name('Given', 'Family', 'Middle', 'Nick',
                                       'Prefix', 'Suffix')

        self.assertTrue(test_name._given, 'Given')
        self.assertTrue(test_name._family, 'Family')


if __name__ == '__main__':
    unittest.main()
