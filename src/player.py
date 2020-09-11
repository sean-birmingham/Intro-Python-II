# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)
        item.on_take()
        self.current_room.items.remove(item)

    def drop_item(self, item):
        self.inventory.remove(item)
        item.on_drop()
        self.current_room.items.append(item)

    def show_inventory(self):
        if len(self.inventory) < 1:
            print('There are no items in your inventory')
        else:
            print('You are carrying:')
            for item in self.inventory:
                print(item.name)
