# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items=[]

    def __str__(self):
        return f'name: {self.name}, current room: {self.current_room}'

    def add_item(self, item):
        self.items.append(item)
        return None

    def del_item(self):
        #TODO
        return NotImplemented

    def get_items(self):
        for i, item in enumerate(self.items):
            print("Item #", i)
            print(item)
    