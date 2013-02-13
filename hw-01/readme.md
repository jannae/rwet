# Homework #1.
>Create a Python program that behaves like a UNIX text processing program (such as cat, grep, tr, etc.). Your program should take text as input (any text, or a particular text of your choosing) and output a version of the text that has been filtered and/or munged. Be creative, insightful, or intentionally banal.

Our homework from last week included a reading from Ron Padgett's book, [*Creative Reading: What It Is, How to Do It, and Why*](http://www.amazon.com/Creative-Reading-What-How-Why/dp/0814109063). One of the exercises that he outlined for "Reading Creatively," which he titled *line looping* sort of stuck with me. The idea was to read every line twice in order to really emphasize rhythm in the text you're reading. His example lead to an almost intuitive generation of standard twelve-bar blues. I loved it. I love the blues. So, I thought that'd be a fun first exercise.

**Bluesify.py** is my first python attempt. It takes in a text (prerequisite: the inputs need consistently spaced line breaks, so poetry works best), and makes it bluesy. Repeats the first line, with bluesy gusto, and segments the piece out into a potential twelve-bar blues format. Code is fully commented.  Ideally this would count beats or syllables, but i'm not there yet. :)

Included are several poems I experimented with. Poems were chosen pretty randomly courtesy of [poets.org](http://www.poets.org). 

Command line code: 

	python bluesify.py < [poem-chosen.txt]
	
A couple of favorite results:

[A Drinking Song, by W. B. Yeats](http://www.poets.org/viewmedia.php/prmMID/21316)

	->python bluesify.py < yeats-drinking.txt 

	Wine comes in at the mouth
	Oooh child, Wine comes in at the mouth
	And love comes in at the eye;
	That’s all we shall know for truth
	
	Before we grow old and die.
	Yeah baby, Before we grow old and die.
	I lift the glass to my mouth,
	I look at you, and I sigh.

And [Carpe Diem, by Robert Frost](http://www.poets.org/viewmedia.php/prmMID/20520)

	->python bluesify.py < frost-carpediem.txt
	
	Age saw two quiet children
	Oooh child, Age saw two quiet children
	Go loving by at twilight,
	He knew not whether homeward,
	
	Or outward from the village,
	Lordy momma, Or outward from the village,
	Or (chimes were ringing) churchward,
	He waited (they were strangers)
	
	Till they were out of hearing
	Yeah baby, Till they were out of hearing
	To bid them both be happy.
	"Be happy, happy, happy,
	
	And seize the day of pleasure."
	Lordy momma, And seize the day of pleasure."
	The age-long theme is Age's.
	'Twas Age imposed on poems
	
	Their gather-roses burden
	Yeah baby, Their gather-roses burden
	To warn against the danger
	That overtaken lovers
	
	From being overflooded
	Lawd tell me, From being overflooded
	With happiness should have it.
	And yet not know they have it.
	
	But bid life seize the present?
	Oooh child, But bid life seize the present?
	It lives less in the present
	Than in the future always,
	
	And less in both together
	Lordy momma, And less in both together
	Than in the past. The present
	Is too much for the senses,
	
	Too crowding, too confusing—
	Oh lawd, Too crowding, too confusing—
	Too present to imagine.