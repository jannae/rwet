# Import my collection of functions for use with nltk.
import nltkjj
import sys
from nltkjj import *

from nltk.corpus import brown
from random import choice, randint

# text = ''
# for line in sys.stdin:
#     text += line
# brown categories: ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

if len(sys.argv) > 1:
	cat = str(sys.argv[1])
	stanzas = int(sys.argv[2])
else:
	cat = 'fiction'
	stanzas = 5

words = brown.words(categories=cat)
sents = brown.sents(categories=cat)
words_tagged = brown.tagged_words(categories=cat)
sents_tagged = brown.tagged_sents(categories=cat)

seps = ['IN','QL','RB','MD','HV','DO','BE','TO']

adjs = get_words(words_tagged,'J')
verbs = get_words(words_tagged,'V')
nouns = get_words(words_tagged,'N')

def ranword(pos):
	if pos == 'J':
		return ran(adjs)
	if pos == 'V':
		return ran(verbs)
	if pos == 'N':
		return ran(nouns)

beckett = '' #start fresh.

# Begin with a random noun from the Brown corpus
start = ran(nouns)
ps = 'J' # used for flipping the part of speech focus. Here we began with a noun, but we want the next word to be an adjective.

# There will be 5 stanzas
for x in range(0, stanzas):
	phrases = []
	# idx variable used to keep track of the focus word when needed.
	idx = start
	# calling up our new focus word.
	start2 = ranword(ps)
	ps = 'N' if ps=='J' else 'J'  #flipping part of speech focus

	beckett += start+'\n'
	beckett += start2+' '
	beckett += start+' '

	# returning list of bigrams related to focus word, de-punctuating the elements in the list
	ib = depunc(ibgram_by_word(words,idx))
	if len(ib) > 0:
		# picking a bigram to return
		beckett += choice(ib)+'\n'
		#shifting index to the bigram
		idx = choice(ib)
	else:
		#randomizing in the case of a non-existant bigram
		beckett += choice(verbs)+'\n'
		#shifting index to the faux bigram when there is none.
		idx = choice(verbs)

	# Find some trigrams from our corpus that relate to our focus word.
	for s in sents_tagged:
		for sep in seps:
			phrase = tgram_by_word(s, idx, sep)
			if len(phrase) > 0:
				phrases.append(phrase)

	if len(phrases) > 0:
		# Pick one.
		ph = choice(phrases)
		beckett += str(ph[0])+' '
	else:
		# Fake one if there are none.
		beckett += ran(adjs)+' '+ran(verbs)+' '+ran(adjs)+' '

	# repeat our original word
	beckett += start+'\n\n'
	# reset our original word to the new word.
	start = start2

	# used for testing proper iteration.
	# print x

#print our poetry!
print beckett