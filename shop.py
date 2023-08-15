from typing import Optional, List

class ShopManager:

    def __init__(self, admin: bool, store_id: Optional[str] = None) -> None:
        self.manager = {}
        self.store_id = store_id
        self.admin_mode = admin

    def add_items(self, items: List[str], store_id: Optional[str] = "Default Store") -> None:
        if not self.admin_mode:
            raise ValueError("You must be an administrator to run this command.")

        if self.store_id is not None:
            self.manager.setdefault(self.store_id, []).extend(items)
        else:
            self.manager.setdefault(store_id, []).extend(items)

    def remove_item(self, item_index: int, store_id: Optional[str] = "Default Store") -> None:
        if not self.admin_mode:
            raise ValueError("You must be an administrator to run this command.")

        store_id = self.store_id if self.store_id else store_id

        if store_id in self.manager and 0 <= item_index < len(self.manager[store_id]):
            self.manager[store_id].pop(item_index)
        else:
            raise ValueError("Store not found or invalid item index.")

    def get_items(self, store_id: Optional[str] = "Default Store") -> List[str]:
        if not self.admin_mode:
            raise ValueError("You must be an administrator to run this command.")

        store_id = self.store_id if self.store_id else store_id

        if store_id in self.manager:
            return self.manager[store_id]
        else:
            raise ValueError("Store not found.")