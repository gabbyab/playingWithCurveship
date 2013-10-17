'A Wild Attempt, a tiny demo game for Curveship.'

__author__ = 'Gabrielle A. Bartomeo'
__copyright__ = 'Copyright 2011 Gabrielle A. Bartomeo'
__license__ = 'ISC'
__version__ = '0.5.0.0'

from item_model import Actor, Room, Thing
from action_model import Modify, Sense
import can
import when

discourse = {
    'metadata': {
        'title': 'A Wild Attempt',
        'headline': 'A tiny demo',
        'people': [('by', 'Gabrielle A. Bartomeo')],
        'prologue': 'Let\'s see if I can make this thing work.'},
    'spin':
    {'commanded': '@me', 'focalizer': '@me', 'narratee': '@me'}}

initial_actions = [Sense('look', '@artist', direct='@classroom', modality='sight')] #8:22 PM

