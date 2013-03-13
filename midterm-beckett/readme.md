#Mechanical Beckett.
##Midterm Project for RWET, 2013.03.13

> This project has two steps. You must:
> 
> * Devise a new poetic form.
> * Create a computer program that generates texts that conform to new poetic form you devised.
> 
> Your poetic form could be something as simple as "Each line must begin with the letter 'A'" or something as sophisticated as Mac Low's diastics.

###Introduction

When approaching this assignment, I thought about conversations we had class concerning the existential nature of computer poetry. It was important to me to experiment with my perspective of algorithmic tools versus creative production, and I wanted to give the computer as much lexical freedom as possible to create on it's own.  The Natural Language Toolkit seemed an appealing place to start, as it contains large amounts of syntatically relevant data in addition to the vocabluary it provides.

I love Samuel Beckett, and his works have always seemed to be a source of inspiration to me. I remembered reading a poem of his ([What is the word](beckett-what.md)) at a young age and imagining him throwing darts at a wall full of words while writing it. This seemed like an ideal source of inspiration for a set of algorithmic guidelines to give a computer to write Beckett-esque poetry with.

Other sources of inspiration: ([Not I](beckett-not-i.md) and [Texts for Nothing #4](beckett-nothing.md))

Stanzas should follow a 1-3-4 word progression. The form is thus:

####Poetic form:

> Noun  
> Descriptor | repeat Noun | directly linked Bigram  
> Trigram for directly linked Bigram | repeat Noun
>
> Descriptor  
> new Noun | repeat Descriptor | directly linked Bigram  
> Trigram for directly linked Bigram | repeat Descriptor
>  
> Begin with new noun, and repeat x times. (experimented with 3, 5 and 7)

####Examples:

	honour
	unclean honour now
	room there now honour

	unclean
	unafraid unclean vessel
	camp-made puffed cagey unclean

	unafraid
	tedious unafraid listen
	one always wakes unafraid

	tedious
	contrary tedious work
	went to work tedious

	contrary
	adamant contrary launch
	inexpensive glittering clever contrary

>

	hills
	callous hills of
	thought first of hills
	
	callous
	blackberry callous formed
	touching whistling healthiest callous
	
	blackberry
	so-called blackberry picking
	picking with him blackberry
	
	so-called
	frederick so-called returned
	came to warn so-called
	
	frederick
	double-breasted frederick sayin
	cuts above any frederick

[Dump of all favorite examples from testing](examples.md)

####Requirements:

[Natural Language Toolkit 2.0](http://nltk.org/) (using the [Brown Corpus](http://icame.uib.no/brown/bcm.html))

	sudo pip install -U numpy
	sudo pip install -U pyyaml nltk
	sudo python -m nltk.downloader -d /usr/share/nltk_data all
	
####Command Line:

	python beckett.py







