import unittest

from categories import get_items_from_category, add_to_category


class MyTestCase(unittest.TestCase):
    def test_get_items_from_category(self):
        mock_categories = {
            'F': ['a', 'b']
        }
        actual = get_items_from_category('F', mock_categories)
        expected = ['a', 'b']
        self.assertEqual(actual, expected)
    def test_not_existing_category(self):
        mock_categories = {}
        actual = get_items_from_category('N', mock_categories)
        expected = []
        self.assertEqual(actual, expected)


    def test_add_to_category(self):
        mock_categories = {
            'a': []
        }
        add_to_category('a', 'newfood', mock_categories)
        self.assertEqual(mock_categories['a'], ['newfood'])






if __name__ == '__main__':
    unittest.main()
