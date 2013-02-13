import sys
import random
from random import choice

# Some init-ing.
outstr = ''
j = 0

# Strip out all of the blank lines from the input text
lines = [i for i in sys.stdin if i[:-1]]

# Some Bluesy phrases for bluesifying!
bluesify = ['Oh lawd', 'Lordy momma', 'Yeah baby', 'Oooh child', 'Lawd tell me']

# Iterate through our text
for i, line in enumerate(lines):
	# tidy up
	line = line.strip()

	# We need to print the line regardless.
	outstr += line
	outstr += '\n'

	# This seems so hacky, I kind of hate it. Could not think of a better way to count two
	# lines away from the bluesified line in order to create a proper stanza.
	j += 1

	# To bluesify, we need to repeat the first line in every stanza
	# (every third line of the input text), and make it bluesy.
	if i % 3 == 0:
		outstr += choice(bluesify)
		outstr += ', '
		outstr += line
		outstr += '\n'
		# Reset our hacky line-distance counter at the beginning of each stanza.
		j = 0

	# When the stanza has reached 4 lines, it needs another line break!
	if j == 2:
		outstr += '\n'

# Print the whole darn thing.
print outstr