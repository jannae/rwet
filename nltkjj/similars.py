import sys
import nltk
import nltk.text
import nltk.corpus

texty = ''
for line in sys.stdin:
    texty += line

idx = nltk.text.ContextIndex([word.lower( ) for word in nltk.corpus.brown.words( )])
save = [ ]
for word in nltk.word_tokenize(texty):
    save.append(idx.similar_words(word))

print set(save)
