import nltk

text = "The little yellow dog barked at the cat"

sentence = nltk.pos_tag(nltk.word_tokenize(text))
pattern = """
	NP: {<DT|PP\$>?<JJ>*<NN>}
		{<NNP>+}
		{<NN>+}
""" # define a tag pattern of an NP chunk
NPChunker = nltk.RegexpParser(pattern) # create a chunk parser
result = NPChunker.parse(sentence) # parse the example sentence
print result # or draw graphically using result.draw()