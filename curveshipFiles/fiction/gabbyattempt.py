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
    {'commanded': '@student', 'focalizer': '@student', 'narratee': '@student'}}

initial_actions = [Sense('examine', '@student', direct='@classroom', modality='sight')] #8:22 PM

items = [
    Actor('@student in @classroom',
        article='the',
        called='student',
        gender='female',
        allowed=can.possess_any_item,
        refuses=[('LEAVE way=(northeast|out)', when.always,
                 '[@student/s] [have/v] code to do')]),

    Room('@classroom',
        article='the',
        called='classroom',
        exits={},
        sight='a paste-colored classroom with an iMac at a table. There is a closed door to the northeast'),

    Thing('@imac in @classroom',
        article='an',
        called='imac',
        sight='the screen of this expensive computer emits a soft light')] # 8:41 PM, check if it works now!

#Lol it blew up... seems to be mad about iMac. Lemme fix. 8:46 PM
#Another error. Keyerror on artist... where...
#Found it. Retrying. 8:48 PM
#Hah... that didn't go as planned! Take a look: (8:50 PM)

#                                    __________
#                                   / Curveship
#                                 version 0.5.0.0
#                        fiction: fiction/gabbyattempt.py



#A WILD ATTEMPT
#A tiny demo
#   by Gabrielle A. Bartomeo

#Let's see if I can make this thing work.

#   You [look at/v] the classroom.

#== Classroom ==

#   A paste-colored classroom with an iMac at a table. There is a closed door to
#the northeast.
#   You see an iMac.