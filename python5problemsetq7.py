#!/usr/bin/env python3
import sys

favs = {'book' : 'Linux for Beginners', 'song' : 'Snooze', 'tree' : 'Evergreen'}
fav_thing4 = 'organism'
favs[fav_thing4] = 'E. coli'

key = sys.argv[1]
print(favs[key])
