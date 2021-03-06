# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = False
        self.lightsource = False

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'

    # def add_item(self, name, description):
    #     item = Item(name=name, description=description)
    #     self.items.append(item)
    #     return None

    def add_item(self, item):
        self.items.append(item)
        return None

    def del_item(self):
        #TODO
        return NotImplemented

    def get_items_names(self):
        items_names=[]
        for item in self.items:
            items_names.append(item.name)
        return items_names
    

    def print_items(self):
        if not self.items:
            print("None")
        for i, item in enumerate(self.items):
            print(f'# {i+1}: {item}')
        # for i, item in enumerate(self.items):
        #     print(f'# {i+1}: {item}\n')
        



    
    
