import sys
import nltk
from nltk import pos_tag, word_tokenize

sample = ''
for line in sys.stdin:
    sample += line

pos_tag(word_tokenize(sample))