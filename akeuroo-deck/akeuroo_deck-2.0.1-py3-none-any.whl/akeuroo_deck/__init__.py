from __future__ import annotations, print_function
from sys import version_info
from enum import Enum, unique
from random import shuffle
from dataclasses import dataclass


__authors__ = "akeuroo"
__license__ = "MIT"
__version__ = "2.0.1"


# Warning the user for the recommended python version
if version_info < (3, 10):
	print("Warning: This module recommends the latest python versions, 3.10+")


@unique
class Suit(Enum):
	CLUB    = "Clubs"
	DIAMOND = "Diamonds"
	HEART   = "Hearts"
	SPADE   = "Spades"

@unique
class Rank(Enum):
	ACE     = 1
	TWO     = 2
	THREE   = 3
	FOUR    = 4
	FIVE    = 5
	SIX     = 6
	SEVEN   = 7
	EIGHT   = 8
	NINE    = 9
	TEN     = 10
	JACK    = 11
	QUEEN   = 12
	KING    = 13


@dataclass
class Card:
	suit: Suit
	rank: Rank

	def __repr__(self) -> str:
		return f"Card({self.suit}, {self.rank})"


VALUE_ERROR_MSG = (
	"Not enough cards in the deck; this issue can "
	"occur when trying to draw/shuffle a empty list."
)


class Deck:
	def __init__(self) -> None:
		self.deck = [
			Card(suit, rank)
			for suit in Suit
			for rank in Rank
		]

	def draw(self):
		if not self.deck:
			raise ValueError(VALUE_ERROR_MSG)

		return self.deck.pop()

	def shuffle(self):
		if not self.deck:
			raise ValueError(VALUE_ERROR_MSG)
		
		shuffle(self.deck)


class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.all = []

	def __call__(self, card: Card):
		if not isinstance(card, Card):
			raise TypeError(f"Can only take a object of type Card and not a {type(card)}")
		
		self.cards.append(card)
		self.value = sum([card.rank.value for card in self.cards])
		self.all = [
			(card.suit.value,
			card.rank.name.title(),
			card.rank.value)
			for card in self.cards
		]