# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # Init player with name
    def _init_(self, name, starting_room):
        self.name = name
    # Player also has attr current_room
        self.current_room = starting_room

    def travel(self, direction):
            # Player should be able to move, add a method for that.

        print(f"Player should travel {direction}")
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")
