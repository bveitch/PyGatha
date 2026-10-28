from __future__ import annotations
from enum import IntEnum

class Characters(IntEnum):
    Green  = 1
    Mustard = 2
    Peacock = 3
    Plum  = 4
    Scarlet = 5
    White  = 6

class Weapons(IntEnum):
    Axe = 7
    Bat = 8
    RollingPin = 9
    NerveAgent = 10
    Knife = 11
    Grenade = 12
    GolfClub = 13
    PlasticBag = 14
    Robot = 15

class Rooms(IntEnum):
    DiningRoom   = 16
    Guesthouse   = 17
    Hall         = 18
    Kitchen      = 19
    Studio       = 20
    Observatory  = 21
    Garden       = 22
    SwimmingPool = 23
    Theatre      = 24

Card = Characters | Weapons | Rooms
number_of_characters = len(Characters)
number_of_weapons = len(Weapons)
number_of_rooms = len(Rooms)
number_of_cards = number_of_characters + number_of_weapons + number_of_rooms
# character_ids= [character.value for character in Characters]
# weapon_ids = [weapon.value for weapon in Weapons]
# room_ids = [room.value for room in Rooms]

# def get_card(card_id: Card):
#     if card_id in Characters:
#         return Characters(card_id)
#     elif card_id in Weapons:
#         return Weapons(card_id)
#     elif card_id in Rooms:
#         return Rooms(card_id)
#     else:
#         ValueError(f"{card_id=} is not a character, weapon or room")

# def get_card(card_id: Card):
#     if card_id in Characters:
#         return Characters(card_id)
#     elif card_id in Weapons:
#         return Weapons(card_id)
#     elif card_id in Rooms:
#         return Rooms(card_id)
#     else:
#         ValueError(f"{card_id=} is not a character, weapon or room")



    