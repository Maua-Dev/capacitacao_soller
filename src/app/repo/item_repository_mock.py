# from typing import Dict, Optional, List

# from ..enums.item_type_enum import ItemTypeEnum
# from ..entities.item import Item
# from .item_repository_interface import IItemRepository


from typing import List

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.item import Item
from ..repo.item_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    items: List[Item]

    def __init__(self):
        self.items = [
            Item("Maçã Dourada", category=ItemTypeEnum.FOOD, item_id = 1, durability = 0.5 ),
            Item("Baú", category=ItemTypeEnum.BLOCK, item_id = 2, durability = 0 ),
            Item("Madeira", category=ItemTypeEnum.BLOCK, item_id = 3, durability = 0 ),
            Item("Machado de Diamante", category=ItemTypeEnum.TOOL, item_id = 4, durability = 0.1 ),

        ]
        
    def get_all_items(self) -> List[Item]:
        return self.items



#     def get_all_items(self) -> List[Item]:
#         return self.items.values()
    
#     def get_item(self, item_id: int) -> Optional[Item]:
#         return self.items.get(item_id, None)
    
#     def create_item(self, item: Item, item_id: int) -> Item:
        
#         self.items[item_id] = item
#         return item
    
#     def delete_item(self, item_id: int) -> Item:
#         item = self.items.pop(item_id, None)
#         return item
        
        
#     def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#         item = self.items.get(item_id, None)
#         if item is None:
#             return None
        
#         if name is not None:
#             item.name = name
#         if price is not None:
#             item.price = price
#         if item_type is not None:
#             item.item_type = item_type
#         if admin_permission is not None:
#             item.admin_permission = admin_permission
#         self.items[item_id] = item
        
#         return item
        
    
    