from collections import Counter
from fantasyGameInventory import display_inventory

def add_to_inventory(inventory, added_items):
    added_item_counter = Counter(added_items)
    added_items_dict = dict(added_item_counter)
    merged_inventory = inventory | added_items_dict
    return merged_inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)