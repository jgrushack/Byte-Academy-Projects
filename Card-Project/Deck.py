import random
from Card import Card

class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.cards = []
		for suit in range(0,4):
			for value in range(0,13):
				card = Card(suit, value)
				self.cards.append(card)


	def __str__(self):
		ret =[]
		for card in self.cards:
			print(str(card))
		return '\n'.join(ret)


	def shuffle(self):
		return random.shuffle(self.cards)

	def drawCard(self):
		return self.cards.pop()

	def numCards(self):
		return len(self.cards)

	def addCard(self, card):
		return self.cards.append(card)
	
	def addToHand(self, hand, numCards)
		pass





deck = Deck()
print(deck)
print ("~~~~~~~~~~~~~~")
print(deck.drawCard())
print ("~~~~~~~~~~~~~~")

x = deck.drawCard()
print (deck)
print ("~~~~~~~~~~~~~~")
print(str(x))
print ("~~~~~~~~~~~~~~")
deck.addCard(x)
print(deck)






