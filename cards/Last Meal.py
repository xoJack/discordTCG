#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Last Meal"
COST = 3
RARITY = 'C'
DESC = "Deal damage to your opponent equal to 25% of their hunger, rounded up."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	enemy.lifeforce = enemy.lifeforce - round( 0.25*enemy.hunger )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

