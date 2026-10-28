from dataclasses import dataclass
from src.cards import Characters, Weapons, Rooms
from termcolor import colored, cprint
class Guess:

    def __init__(self, 
                character: Characters,
                weapon: Weapons ,
                room: Rooms,
                is_mystery: bool = False ):
        self.character = character
        self.weapon = weapon
        self.room = room
        self.is_mystery = is_mystery

    def __eq__(self, other):
        if self.character != other.character:
            return False
        elif self.weapon != other.weapon:
            return False
        elif self.room != other.room:
            return False
        return True

    def print(self):
        if self.is_mystery:
            background = "on_white"
        else:
            background = "on_blue"
        cprint(f'{self.character.name, \
                 self.weapon.name, \
                 self.room.name}', 'black', background)