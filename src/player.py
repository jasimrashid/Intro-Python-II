# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items=[]
        self.score=100

    def __str__(self):
        return f'name: {self.name}, current room: {self.current_room}'

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
        
