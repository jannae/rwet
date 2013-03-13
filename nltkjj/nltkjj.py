from __future__ import division

import nltk, re, pprint
from nltk.book import *
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus import brown

from urllib import urlopen

def surl(url):
	return urlopen(url).read()

def lex_diversity(text):
	return len(text) / len(set(text))

def pct(count,total):
	return 100*count/total

def get_rare(text):
	fdist = FreqDist(text)
	rares = fdist.hapaxes()
	return sorted(rares)

def get_longs(longst,text):
	# longst = min length of word desired
	# text = text to be analyzed
	V = set(text)
	longs = [wo for wo in V if len(wo) > longst]
	return sorted(longs)

def get_freq_longs(flongst,longst,text):
	# flongst = min frequency of long word desired
	# longst = min length of word desired
	# text = text to be analyzed
	fdist = FreqDist(text)
	flongs = [w for w in set(text5) if len(w) > longst and fdist5[w] > flongst]
	return sorted(flongs)

def whatsin_guten():
	for fileid in gutenberg.fileids():
		num_chars = len(gutenberg.raw(fileid)) 
		num_words = len(gutenberg.words(fileid))
		num_sents = len(gutenberg.sents(fileid))
		num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
		print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

def longest_sent(text):
	longest_len = max([len(s) for s in gutenberg.sents(text)])
	return [s for s in gutenberg.sents(text) if len(s) == longest_len]

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

def getsim(sim):
	texts = nltk.text.ContextIndex([word.lower( ) for word in nltk.corpus.brown.words( )])
	sims = [ ]
	for word in nltk.word_tokenize("i want to solve this problem"):
    	sims.append(texts.similar_words(word))


	text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
	return text.similar(sim)