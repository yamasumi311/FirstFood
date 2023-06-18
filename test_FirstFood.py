from unittest import TestCase

from functions import check_array_contains


class Test(TestCase):
    def test_check_items(self):
        self.assertTrue(check_array_contains('potato', []))

    def test_existing_item(self):
        self.assertFalse(check_array_contains('potato', ['potato']))

    def test_new_item(self):
        self.assertTrue(check_array_contains('tomato', ['potato']))