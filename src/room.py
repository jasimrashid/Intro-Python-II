# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f'name: {self.name}, description: {self.description}'

    def add_item(self, name, description):
        item = Item(name=name, description=description)
        self.items.append(item)
        return None

    def del_item(self):
        #TODO
        return NotImplemented

    def get_items(self):
        for i, item in enumerate(self.items):
            print("Item #", i+1)
            print(item)



    
    
