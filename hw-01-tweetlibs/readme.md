# Homework #1. Tweetlibs.
>Create a Python program that behaves like a UNIX text processing program (such as cat, grep, tr, etc.). Your program should take text as input (any text, or a particular text of your choosing) and output a version of the text that has been filtered and/or munged. Be creative, insightful, or intentionally banal.

As per my normal instinct when learning any program languages, I couldn't wait to get python talking to the internet.

Rather than diving into any complicated auth issues that usually come up with using Twitter, I'm simply leveraging their public search.rss query functionality. Easy to use and requires no API key and all that jazz. 

### Requirements

[Feedparser](http://code.google.com/p/feedparser/) (may need sudo here)

	sudo pip install feedparser

#### Command line code: 

	python tweetlib.py
	
User is then prompted for a query term, and a term to replace it with.

	Search for tweets about:
	Madlib it with:
	
A couple of amusing results:
	
	Replacing "boehner" with "unicorns"...
	
	lauer asks unicorns about these dc kids would view congress, w/ so few black lawmakers. worth noting that only 19% of kids in dc are white.
	
	suddenly i find myself wishing i could shave unicorns's eyebrows
	
	unicorns says no to minimum wage increase
	
	unicorns: 'hard to imagine' budget agreement http://t.co/u8kxsvbe #business #biznews #ap
	
And:

	Replacing "obama" with "kittens"...
	
	'no one working full time should be living in poverty!' president kittens #sotu2013
	
	anonymous threatens to hack kittens's state of the union broadcast http://t.co/ywpfsj2f
	
	why kittens's executive order on cybersecurity doesn't satisfy most experts http://t.co/ipf1hbfk #cybersec #datasec #sotu
	
	join the state of the union: fireside hangout with president kittens on february 14.
