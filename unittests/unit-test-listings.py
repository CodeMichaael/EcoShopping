import unittest
from datetime import date
from listing import ListingManager

class TestListingManager(unittest.TestCase):

    def setUp(self):
        self.manager = ListingManager(admin_mode=True)

    def test_get_new_listing(self):
        result = self.manager.get_new_listing("Test Store", ["Item 1", "Item 2"])
        expected = {
            f"Store: Test Store": "Items in store: Item 1, Item 2",
            "Date: ": f"{date.today()}"
        }
        self.assertEqual(result, expected)
        self.assertEqual(len(self.manager.manager), 1)
        self.assertEqual(len(self.manager.get_items("Test Store")), 2)

    def test_search_listing_found(self):
        self.manager.get_new_listing("Test Store", ["Item 1", "Item 2"])
        result = self.manager.search_listing("Test Store")
        expected = {
            f"Store: Test Store": "Items in store: Item 1, Item 2",
            "Date: ": f"{date.today()}"
        }
        self.assertEqual(result, expected)

    def test_search_listing_not_found(self):
        result = self.manager.search_listing("Nonexistent Store")
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
