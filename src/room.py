# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def look(self):
        if len(self.items) > 0:
            print(f'There are {len(self.items)} items in this room:')
            for i in self.items:
                print(i.name)
        else:
            print('There are no items in this room')
