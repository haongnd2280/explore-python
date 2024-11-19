# Python3.11

from dataclass import dataclass 


@dataclass 
class InventoryItem:
    """Class for keeping track of an item in inventory.
    """

    name: str
    unit_price: float
    quantity_on_hand: int = 0    # available quantity

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


    # This class will add, among other things, a __init__() that looks like:
    # def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    #     self.name = name
    #     self.unit_price = unit_price
    #     self.quantity_on_hand = quantity_on_hand
