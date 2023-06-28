import unittest

from categories import get_items_from_category, add_to_category, remove_from_category


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


    def test_add_to_category_will_filter_away_duplicate(self):
        mock_categories = {
            'a': []
        }
        add_to_category('a', 'newfood', mock_categories)
        add_to_category('a', 'newfood', mock_categories)
        self.assertEqual(mock_categories['a'], ['newfood'])

    def test_remove_from_category(self):
        mock_categories = {
            'a': ['b']
        }
        remove_from_category('a', 'b', mock_categories)
        self.assertEqual(mock_categories['a'], [])

    def test_remove_from_category_2(self):
        mock_categories = {
            'c': ['d'],
            'a': ['b']
        }
        remove_from_category('a', 'b', mock_categories)
        self.assertEqual(mock_categories['a'], [])

    def test_removing_food_twice(self):
        mock_categories = {
            'a': ['b']
        }
        remove_from_category('a', 'b', mock_categories)
        remove_from_category('a', 'b', mock_categories)
        self.assertEqual(mock_categories['a'], [])

    def test_removing_not_existing_food(self):
        mock_categories = {
            'a': ['b']
        }
        remove_from_category('a', 'c', mock_categories)
        self.assertEqual(mock_categories['a'], ['b'])

    def test_removing_from_not_existing_category(self):
        mock_categories = {
            'a': ['b']
        }
        remove_from_category('c', 'b', mock_categories)
        self.assertEqual(mock_categories['a'], ['b'])


if __name__ == '__main__':
    unittest.main()
