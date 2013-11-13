# Let's see how badly I can mess this up. C:

'Losing the Game'

__author__ = 'Gabrielle A. Bartomeo'
__copyright__ = 'Copyright 2011 Gabrielle A. Bartomeo'
__license__ = 'ISC'
__version__ = '0.5.0.0'

from random import random, randint, choice
import datetime

from item_model import Actor, Door, Room, SharedThing, Substance, Thing
from action_model import Behave, Configure, Modify, Sense
from joker import update_spin
import can
import when

discourse = {
	'metadata': {
		'title': "Losing the Game",
		'headline': "Still confused",
		'people': [('by', 'Gabby')],
		'prologue': 'You find yourself coming to and out of the darkness.'
	},
	'spin': {
	'commanded': "@player",
	'focalizer': "@player",
	'narratee': "@player"
	}
}

initial_actions = [Sense('look', '@player', direct='@beach', modality='sight')]

currentTime = datetime.datetime.now().minute%10

class OutsideArea(Room):
    'Subclass for all forest/outside Rooms, with sky and sun or moon.'

    def __init__(self, tag, **keywords):
        if 'shared' not in keywords:
            keywords['shared'] = []
        keywords['shared'] += ['@sky', '@moon', '@sun']
        Room.__init__(self, tag, **keywords)


class HeavenlyBody(SharedThing):
	'Stars, moon, sun, planets if needed, huzzah.'

	def __init__(self, tag, **keywords):
		self.alive = False
		Thing.__init__(self, tag, **keywords)
        #put in something with light


class Sun(HeavenlyBody):
	'The sun, the only instance of... the sun.'

	def react(self, world, basis):
		actions = []
		if currentTime < 4:
			actions.append(Modify('look', basis.agent, direct=str(self), feature='prominence', new=1.0))
			actions.append(Modify('look', basis.agent, direct=str(self), feature='mention', new=True))
		else:
			actions.append(Modify('look', basis.agent, direct=str(self), feature='prominence', new=0.0))
			actions.append(Modify('look', basis.agent, direct=str(self), feature='mention', new=False))
		actions.append(Modify('look', basis.agent, direct=str(self), feature='glow', new=1.0))
		return actions + HeavenlyBody.react(self, world, basis)


class Moon(HeavenlyBody):
	'The moon, the only instance of... the moon.'

	def react(self, world, basis):
		actions = []
		if currentTime > 4:
			actions.append(Modify('look', basis.agent, direct=str(self), feature='prominence', new=1.0))
			actions.append(Modify('look', basis.agent, direct=str(self), feature='mention', new=True))
		else:
			actions.append(Modify('look', basis.agent, direct=str(self), feature='prominence', new=0.0))
			actions.append(Modify('look', basis.agent, direct=str(self), feature='mention', new=False))
		actions.append(Modify('look', basis.agent, direct=str(self), feature='glow', new=1.0))
		return actions + HeavenlyBody.react(self, world, basis)

class Tree(Thing):
	treeSmacked = 0
	def react(self, world, basis):
		actions = []
		if basis.verb in ['strike', 'punch', 'hit'] and basis.direct == str(self):
			self.treeSmacked = self.treeSmacked + 1
			print self.children
			if self.treeSmacked < 17 and self.treeSmacked % 4 == 0:
				actions.append(Modify('open', str(self), direct=str(self), feature='open', new=True))
				actions.append(Configure('drop','@tree', direct='@log' + str((self.treeSmacked/4)-1), template=['[direct/o] [fall/v] off [agent/s]'], new=('in', '@beach') ))
				actions.append(Modify('close', str(self), direct=str(self), feature='open', new=False))
			#FIND A WAY TO MAKE IT SO THE TREE'S GONE AFTER BEING HIT 16 times!
		return actions + Thing.react(self, world, basis)



items = [
	Actor('@player in @beach',
		article = "the",
		called = "player",
		gender = "female",
		allowed = can.possess_any_item),

	OutsideArea('@beach',
		article ='the',
		called ="beach",
		sight ="A sprawling beach with glittering sand and waves crashing at the shore.",
		exits = {}),

	Sun('@sun in @sky',
		article = 'the',
		called = "sun",
		sight = "Hard to look at and ever generous in its light giving warmth, the sun sits far out of reach."
		),

	Moon('@moon in @sky',
		article = 'the',
		called = 'moon',
		sight = 'Softly glowing in the darkness of the sky, this pale white orb strolls leisurely across the aerial landscape.',
		),

	SharedThing('@sky',
		article = 'the',
		called = 'sky',
		sight = 'Covering the vast expanse far above is an air-made sea of varying blues.'
		),

	Tree('@tree in @beach', 
		article = 'a', 
		called= 'tree', 
		open= False,
		sight = 'A tree that is twice your height with green leaves.'),

	Room('@dummyroom',
		called = 'dummyroom',
		sight = 'throw stuff here',
		exits = {})

]



for everyNum in range(50):
	items.append(Thing('@sand' + str(everyNum) + ' in @beach', article = 'some', called = 'sand', sight = 'It is grainy and fine with a pale tan color.', taste = 'that the sand has the same flavor as salt.', mention= False))


for everyNum in range(4):
	items.append(Thing('@log' + str(everyNum) + ' in @tree', article= 'a', called = 'log', sight ='It is a wooden log'))