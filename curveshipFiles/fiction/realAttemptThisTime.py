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
		'prologue': 'You find yourself coming to out of the darkness.'
	},
	'spin': {
	'commanded': "@player",
	'focalizer': "@player",
	'narratee': "@player"
	}
}

initial_actions = [Sense('look', '@player', direct='@beach', modality='sight')]

class OutsideArea(Room):
    'Subclass for all forest/outside Rooms, with sky and sun or moon.'

    def __init__(self, tag, **keywords):
        if 'shared' not in keywords:
            keywords['shared'] = []
        keywords['shared'] += ['@sky', '@sunmoon']
        Room.__init__(self, tag, **keywords)

class HeavenlyBody(Thing):
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
			actions.append(Modify('change_appearance', basis.agent, direct=str(self), feature='sight', new="hard to look at and ever generous in its light giving warmth, the sun sits far out of reach"))
		else:
			actions.append(Modify('change_prominence', basis.agent, direct=str(self), ))

currentTime = datetime.datetime.now().minute%10

"""
def lookAtSunMoon():
	
	if currentTime < 4:
		timeOfDay = "day"
		sunMoonObj = "sun"
	else:
		timeOfDay = "night"
		sunMoonObj = "moon"
	return sunMoonObj"""


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

	SharedThing('@sunmoon',
		article = 'the',
		called = lookAtSunMoon(),
		sight = "a bright luminous object in the sky"
		),

	SharedThing('@sky',
		article = 'the',
		called = 'sky',
		sight = 'Covering the vast expanse far above is an air-made sea of varying blues.')
]