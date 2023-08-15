import unittest
from shop import ShopManager

class TestShopManager(unittest.TestCase):

    def test_add_items(self):
        manager = ShopManager(admin=True)
        manager.add_items(["item1", "item2"])
        self.assertEqual(manager.get_items(), ["item1", "item2"])

    def test_remove_item(self):
        manager = ShopManager(admin=True)
        manager.add_items(["item1", "item2"])
        manager.remove_item(0)
        self.assertEqual(manager.get_items(), ["item2"])

    def test_get_items(self):
        manager = ShopManager(admin=True)
        manager.add_items(["item1", "item2"])
        self.assertEqual(manager.get_items(), ["item1", "item2"])

    def test_invalid_remove_item(self):
        manager = ShopManager(admin=True)
        manager.add_items(["item1", "item2"])
        with self.assertRaises(ValueError):
            manager.remove_item(5)

    def test_non_admin_add_items(self):
        manager = ShopManager(admin=False)
        with self.assertRaises(ValueError):
            manager.add_items(["item1", "item2"])

    def test_non_admin_remove_item(self):
        manager = ShopManager(admin=False)
        with self.assertRaises(ValueError):
            manager.remove_item(0)

    def test_non_admin_get_items(self):
        manager = ShopManager(admin=False)
        with self.assertRaises(ValueError):
            manager.get_items()

if __name__ == '__main__':
    unittest.main()
