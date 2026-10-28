from random import seed, shuffle
from src.cards import Characters, Weapons, Rooms
from src.player import BasePlayer
from src.guess import Guess

def get_mystery(fixed_seed=None):
    deck = []
    if fixed_seed is not None:
        seed(fixed_seed)
    weapons = list(Weapons)
    shuffle(weapons)
    weapon = weapons.pop()
    deck.extend(weapons)
    characters = list(Characters)
    shuffle(characters)
    character = characters.pop()
    deck.extend(characters)
    rooms = list(Rooms)
    shuffle(rooms)
    room = rooms.pop()
    deck.extend(rooms)
    mystery = Guess(character, weapon, room, is_mystery=True)
    return mystery, deck


# def deal(players: list[BasePlayer]) -> Guess:
#     mystery, deck = get_mystery()
#     deck = shuffle(deck)
#     for i, card in enumerate(deck):
#         iplayer = i % len(players)
#         players[iplayer].deal(card)
#     return mystery

def deal(players: dict[str,list], fixed_seed=None) -> tuple:
    mystery, deck = get_mystery(fixed_seed = fixed_seed)
    shuffle(deck)
    for i, card in enumerate(deck):
        iplayer = i % len(players)
        player_name = list(players.keys())[iplayer]
        players[player_name].append(card)
    return mystery

class Game:

    def __init__(self, players: list[BasePlayer]):
        self._num_players = len(players)
        self._players = players
        self._records = []
        self._mystery = deal(self._players)

    def play(self):
        game_over = False
        i = 0
        winner = None
        while not game_over:
            iplayer = i % self._num_players
            detective = self._player[iplayer]
            if detective.disqualified() is False: 
                suspect = detective.suspect()
                for j in range(1, self._num_players):
                    jplayer = (iplayer +j) % self._num_players 
                    response = self._player[jplayer].respond(suspect)
                    if response is not None:
                        self._records.append([iplayer, suspect, jplayer, True])
                        detective.alibi(response)
                        break
                    else:
                        self._records.append([iplayer, suspect, jplayer, False])
                if detective.accuse() is not None:
                    accusation = detective.accuse()
                    if accusation == self._mystery:
                        game_over = True
                        winner = detective
                    else:
                        detective.disqualified()
            i+=1 
        if game_over:
            print(f"end of game : {winner.name} wins!")

            





