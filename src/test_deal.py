
import os
import sys

# Adds the parent directory of 'src' to the search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import deal
from src.player import BasePlayer
from termcolor import colored, cprint

def run_deal_4():
    player_names = ["andrea", "boris", "charly", "dave"]
    #players = [ BasePlayer(name) for name in player_names]
    players = { name: [] for name in player_names}
    mystery = deal(players, 42)
    mystery.print()
    for name, cards in players.items():
        cardnames = [ card.name for card in cards]
        print(f"{name} : {cardnames}")

def run_deal_5():
    player_names = ["andrea", "boris", "charly", "dave", "emily"]
    #players = [ BasePlayer(name) for name in player_names]
    players = { name: [] for name in player_names}
    mystery = deal(players, 42)
    mystery.print()
    for name, cards in players.items():
        cardnames = [ card.name for card in cards]
        print(f"{name} : {cardnames}")
        for i, name in enumerate(cardnames):
            if i == len(cardnames) -1:
                end = "\n"
            else:
                end = ", "
            cprint(name, 'green', 'on_black', end=end)
def run_deal_6():
    player_names = ["andrea", "boris", "charly", "dave", "emily", "freddy"]
    #players = [ BasePlayer(name) for name in player_names]
    players = { name: [] for name in player_names}
    mystery = deal(players, 42)
    mystery.print()
    for name, cards in players.items():
        cardnames = [ card.name for card in cards]
        print(f"{name} : {cardnames}")

if __name__== "__main__": 
    run_deal_4()
    run_deal_5()
    run_deal_6()