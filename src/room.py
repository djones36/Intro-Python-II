# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def _initi_(self, name, description)
    #Name, description
    self.name = name
    self.description = description
    # n_to,s_to,e_to,w_to
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

    def _str_(self):
        return f"\n{self.name}\n\n{self.description}"

    def get_room_in_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to:
        else:
            return None
