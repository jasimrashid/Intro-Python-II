class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.value = 0

    def __str__(self):
        return f'name: {self.name}, description: {self.description}'

    def on_take(self):
        print(f"You picked up {self.name}.")

    def on_drop(self):
        print(f"You dropped {self.name}.")

class Treasure(Item):
    def __init__(self, type, name, description):
        super().__init__(name,description)
        self.type = type
        # my_dictionary = dict(map(lambda kv: (kv[0], f(kv[1])), my_dictionary.iteritems()))
        # type: gold, silver, bronze, diamond.
        self.mapping  = {
            'bronze': 20,
            'silver': 50,
            'gold': 100,
            'diamond': 500
        }

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def on_drop(self):
        print(f"It is not wise to drop your source of light!")

    