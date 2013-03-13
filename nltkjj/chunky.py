import nltk
import nltk.chunk
import itertools

class TagChunker(nltk.chunk.ChunkParserI):
    def __init__(self, chunk_tagger):
        self._chunk_tagger = chunk_tagger

    def parse(self, tokens):
        # split words and part of speech tags
        (words, tags) = zip(*tokens)
        # get IOB chunk tags
        chunks = self._chunk_tagger.tag(tags)
        # join words with chunk tags
        wtc = itertools.izip(words, chunks)
        # w = word, t = part-of-speech tag, c = chunk tag
        lines = [' '.join([w, t, c]) for (w, (t, c)) in wtc if c]
        # create tree from conll formatted chunk lines
        return nltk.chunk.conllstr2tree('\n'.join(lines))

sentence = "This is a good enough sentence for all the girls and boys."

# sentence should be a list of words
tagged = tagger.tag(sentence)
tree = chunker.parse(tagged)
# for each noun phrase sub tree in the parse tree
for subtree in tree.subtrees(filter=lambda t: t.node == 'NP'):
    # print the noun phrase as a list of part-of-speech tagged words
    print subtree.leaves()