# Project Module 5: Simple Inventory System

# Create an inventory management system for a small store.
# Focus on object-oriented programming concepts.

# Example Code:

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item}")

    def view_inventory(self):
        for item in self.items:
            print(item)

# Example usage
inventory = Inventory()
item1 = Item("Apples", 10)
item2 = Item("Bananas", 5)
inventory.add_item(item1)
inventory.add_item(item2)
inventory.view_inventory()
