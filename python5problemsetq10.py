#!/usr/bin/env python3

import sys

category = sys.argv[1]
category = str(category)
item = sys.argv[2]
item = str(item)

favs = {'book' : 'Linux for Beginners', 'song' : 'Snooze', 'tree' : 'Evergreen'}
print(favs)
favs[category] = item
print(favs)

x = input('Change the value of your category:')
favs[category] = x
print("You have successfully changed the value to",x)
print(favs)