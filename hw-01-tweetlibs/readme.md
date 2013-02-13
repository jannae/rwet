# Homework #1. Tweetlibs.
>Create a Python program that behaves like a UNIX text processing program (such as cat, grep, tr, etc.). Your program should take text as input (any text, or a particular text of your choosing) and output a version of the text that has been filtered and/or munged. Be creative, insightful, or intentionally banal.

As per my normal instinct when learning any program languages, I couldn't wait to get python talking to the internet.

Rather than diving into any complicated auth issues that usually come up with using Twitter, I'm simply leveraging their public search.rss query functionality. Easy to use and requires no API key and all that jazz. 

### Requirements

[Feedparser](http://code.google.com/p/feedparser/) (may need sudo here)

	sudo pip install feedparser

Command line code: 

	python tweetlib.py
	
User is then prompted for a query term for 

	Search for tweets about:
	Madlib it with:
	
A couple of amusing results:

