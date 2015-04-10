class Card(object):
	"""Represents a standard playing card """
	values = ["Ace","2","3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	suits =["Hearts", "Clubs", "Spades", "Diamonds" ]
	
	def __init__(self, suit = 0, value = 2):

		self.suit = suit
		self.value = value