import nltk
import re
import sys
import random
import string

from nltk.corpus import brown
from random import choice, randint

# text = ''
# for line in sys.stdin:
#     text += line

def process_text(srctxt):
	#tested, works.
	#returns set of properly tokenized large piece of text
	sents = nltk.sent_tokenize(srctxt)
	sents = [nltk.pos_tag(sent) for sent in sents]
	sents = [nltk.word_tokenize(sent) for sent in sents]
	return sents

def get_words(words_tagged,tag_prefix):
	words = []
	for (word, tag) in words_tagged:
		if tag.startswith(tag_prefix):
			words.append(word.lower())
	return list(set(words))

def get_tags(words_tagged,tag_prefix):
	# cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in words_tagged if tag.startswith(tag_prefix))
	# return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())
	tags = []
	for (word, tag) in words_tagged:
		if len(tag_prefix) > 0:
			if tag.startswith(tag_prefix):
				tags.append(tag)
		else:
			tags.append(tag)
	return list(set(tags))

def tgram_by_tag(sents_tagged,tag_pre1,sep,tag_pre2):
	tgrams = []
	for (word1,tag1), (word2,tag2), (word3,tag3) in nltk.trigrams(sents_tagged):
		if (tag1.startswith(tag_pre1) and tag2 == sep and tag3.startswith(tag_pre2)):
			tgrams.append(word1.lower() +' '+ word2.lower() +' '+ word3.lower())
	return list(set(tgrams))

def tgram_by_word(sents_tagged,inword1,sep):
	tgrams = []
	for (word1,tag1), (word2,tag2), (word3,tag3) in nltk.trigrams(sents_tagged):
		if (word1 == inword1 and tag2 == sep) or (word3 == inword1 and tag2 == sep):
			tgrams.append(word1.lower() +' '+ word2.lower() +' '+ word3.lower())
	return list(set(tgrams))

def ibgram_by_word(words,rel_word):
	return list(set(word2.lower() for (word1, word2) in nltk.ibigrams(words) if word1 == rel_word))

def ran(listy):
	if len(listy) > 0:
		return listy.pop(random.randrange(len(listy)))

def depunc(listy):
	listy = [''.join(c for c in s if c not in string.punctuation) for s in listy]
	listy = [s for s in listy if s]
	return listy



# for testing process_text function. WORKS.
# text = process_text(text)
# print get_verbs(text)
# print get_words(text,'VD')
# tagged = findtags('V',text)
# for tag in sorted(tagged):
# 	print tag, tagged[tag]

# for s in sents_tagged:
# 	phrase = tgram_by_tag(s,'N','IN','V')
# 	if len(phrase) > 0:
# 		test.append(phrase)
# if len(test) > 0:
# 	ph = test.pop(randint(1,len(test)))
# 	print ph[0]

# http://nltk.googlecode.com/svn/trunk/doc/book/ch05.html

# print sorted(set(b for (a, b) in nltk.ibigrams(text) if a == 'often'))

# here, I'm trying to get a verb phrase, separated by the tag "to"
# From:

# brown categories: ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
cat = 'fiction'

words = brown.words(categories=cat)
sents = brown.sents(categories=cat)
words_tagged = brown.tagged_words(categories=cat)
sents_tagged = brown.tagged_sents(categories=cat)

seps = ['IN','QL','RB','MD','HV','DO','BE','TO']

adjs = get_words(words_tagged,'J')
verbs = get_words(words_tagged,'V')
nouns = get_words(words_tagged,'N')

beckett = ''

# There will be 7 stanzas

for x in range(0, 7):
	phrases = []
	begn = ran(nouns)
	idx = begn

	# beckett += str(x)+': '
	beckett += begn+'\n'
	beckett += ran(adjs)+' '
	beckett += begn+' '

	ib = depunc(ibgram_by_word(words,begn))
	if len(ib) > 0:
		beckett += choice(ib)+' '
		idx = choice(ib)
	else:
		beckett += choice(verbs)+' '
		idx = choice(verbs)

	beckett += '\n'
	for s in sents_tagged:
		for sep in seps:
			phrase = tgram_by_word(s, idx, sep)
			if len(phrase) > 0:
				phrases.append(phrase)
				
	if len(phrases) > 0:
		ph = choice(phrases)
		beckett += str(ph[0])+' '
	else:
		beckett += ran(adjs)+' '+ran(verbs)+' '+ran(adjs)+' '

	beckett += begn+'\n\n'
	print x

print beckett
