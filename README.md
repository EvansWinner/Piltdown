# Piltdown

*"Making your mindless Twitter propaganda look more scientific since 2021!"*


## Introduction (or, what is it? and what's it for?)

Tweeviz is a tiny, nay, even trivial Python library
that generates Unicode strings of bar charts
and some other data visualization thingies
which are meant to be included in your Twitter posts.

Here is an example:

> FIXME: Write library and create an example.

Here are all the kinds of charts and graphs and stuff
you can include in your tweets as simple Unicode text:

> FIXME: Implement some....

But see all the caveats.
I mean, they're pretty obvious.
There is only so much you can do with nothing but text
that is always right-justified,
displayed in a very narrow column, 
and in a variable-width font--
even with Unicode.

I wrote this for the fun of it,
on a lark. Don't get all testy with me.


## The Basic Idea

For most of the types of plot, you will specify your data set,
(typically a list, list of tuples, dict, etc.).
Generating this from a datafrane or other form is your problem--
Tweeviz just generates strings. That's all.
There are a million utilities that could be included 
to post your string to Twitter for you,
or to do other Unicode tricks,
like bold or italics,
but at least for the moment
Tweeviz wants to do one thing and do it (tollerably) well:
generate strings that work as data viz in the space of a tweet.
That means generally just the graphic elements and sometimes axis labels.
Titles and keys are mostly your problem.
But the idea is that all you have to do is concatenate any string you want 
with the output of your Tweeviz graph,
and thereby do we identify Bob as your parent's brother.


# The Plots

For each of the entries below, we assume you have already done something like

> from tweeviz import bar

-- for example if you are using the bar() function to create a bar chart.

There is nothing to import except one top-level function
with a name like that.


## Dot Chart

Not to be confused with a dot plot.
This is the kind of thing they use on Khan Acadamy
to teach small children about data.
FIXME: Actually verify the name and all that.

**Example**

> FIXME

# Installation

Clone the repository, and import tweeviz from the root directory
or add it to your Python path, or however you do it.
I blew a full day trying to figure out how to get Python's
module system to work the way I wanted it, and it's my way
or the highway, so there is no pip package unless someone
tells me how to organize my source code the way I want it.

Ok, but for real, do

> >>> import tweeviz as tv

and then you can, for example, do,

> >>> tv.bar(mydict,mywidth)

and it will return a bar chart as a string.


# Hacking

Project goals:

 - Simple
 - Really simple
 - Simple enough to just write static documentation here.
 - Don't try to do anything but create the charts and graphs.
   Just functions that return strings.
   Leave Twitter posting, statistical preprocessing,
   and mixing output with other strings (titles, general writting, etc.)
   to the user/other libraries.
 - Easy to use.
 - Just focused on the Twitter use case.
   Not a general solution to the ASCII-art data viz problem,
   which is never-ending.
