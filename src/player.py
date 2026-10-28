from abc import ABC, abstractmethod
from src.cards import Card
from src.guess import Guess

class BasePlayer(ABC):

    def __init__(self, name):
        self._name = name
        self._cards = []

    def deal(self, card):
        self._cards.append(card)

    @abstractmethod
    def suspect(self) -> Guess:
        raise NotImplemented

    @abstractmethod
    def accuse(self) -> Guess:
        raise NotImplemented

    @abstractmethod
    def respond(self, guess: Guess) -> None | Card:
        raise NotImplemented

# def SimplePlayer(BasePlayer):

#      def __init__(self, name, other_players=List[]):
#          self._name = name
#          self._domains = []

#      def add_note(self,):

#      def suspect(self):
