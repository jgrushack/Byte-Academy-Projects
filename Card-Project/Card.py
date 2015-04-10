class Card():
	"""Represents a standard playing card """
	values = ["Ace","2","3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	suits =["Hearts", "Clubs", "Spades", "Diamonds" ]
	
	def __init__(self, suit, value):

		self.suit = suit
		self.value = value

	def __str__(self):
		return '%s of %s' % (Card.values[self.value],Card.suits[self.suit])
