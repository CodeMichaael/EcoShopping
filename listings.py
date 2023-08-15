from typing import Optional, List
from shop import ShopManager
import datetime

class ListingManager(ShopManager):

    def __init__(self, admin_mode: Optional[bool] = False) -> None:
        self.admin_mode = admin_mode
        self.manager = {}
        self.instance = ShopManager(True)
    
    def get_new_listing(self, listing_name: str, items: List[any]) -> None:
        if not self.admin_mode:
            raise ValueError("You must be an administrator to run this command.")

        self.instance.add_items(items, listing_name)
        result = self.instance.get_items(listing_name)
        items_found = ", ".join(result)

        listing_format = {

            f"Store: {listing_name}": f"Items in store: {items_found}",
            "Date: ": f"{datetime.date.today()}" 
        }

        self.manager[listing_name] = listing_format
        return listing_format

    def search_listing(self, listing_name: str) -> dict:
        if listing_name in self.manager:
            result = [item for item in self.manager[listing_name]]
            return result
        else:
            return {} 