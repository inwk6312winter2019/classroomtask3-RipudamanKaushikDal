
import random
class Card():
	rank_names=[None,'Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
	suit_names=['Clubs','Diamonds','Hearts','Spades']

	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank

	def __str__(self):
		return f"{self.rank_names[self.rank]} of {self.suit_names[self.suit]}"

class Deck():
	def __init__(self):
		self.cards=[]
		for suit in range(4):
			for rank in range(1,14):
				card= Card(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res=[]
		for cards in self.cards:
			res.append(str(cards))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self,card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def play(self):
		i=0
		player1=[]
		player2=[]
		pile=[]
		self.shuffle()
		for j in range(20):
			player1.append(self.pop_card())

		for c in player1:
			self.add_card(c)

		self.shuffle()

		for k in range(20):
			player2.append(self.pop_card())

		while i<10:
			turn1=player1.pop(i)
			turn2=player2.pop(i)
			print(turn1,'\t',turn2)
			if pile==[]:
				pile.extend((turn1,turn2))
			else:
				if turn1==pile[-1]:
					for item in pile:
						player1.append(item)
					pile=[]
				pile.append(turn1)
				if turn2==pile[-1]:
					for items in pile:
						player2.append(items)
					pile=[]
				pile.append(turn2)
			i+=1
		print(len(pile))
		if len(player1) > len(player2):
			print("Congrats to player1,You've won with",len(player1),"cards left")
		elif len(player2) > len(player1):
			print("Congrats to player2,You've won",len(player2),"cards left")
		else:
			print("It's a tie")
d=Deck()
d.play()
