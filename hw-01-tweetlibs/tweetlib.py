# Requires feedparser (pip install feedparser)

import feedparser

term = raw_input("Search for tweets about: ").lower()
query = term.replace (' ', '+')
madlib = raw_input("Madlib it with: ").lower()

feed = feedparser.parse("http://search.twitter.com/search.atom?q=" + query)

print('\nReplacing "'+term+'" with "'+madlib+'"...\n')

for i in feed.entries:
	tweet = i.title.lower()

	if not tweet.startswith('rt'):
		tweet = tweet.strip()
		tweet = tweet.replace(term,madlib)
		print(tweet)
		print(i.link+'\n')