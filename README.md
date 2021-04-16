# Piltdown

<img src="Piltdown_man.jpg" width="100px" align="right" alt="Piltdown Man"/>

*"Making your mindless Twitter propaganda look more scientific since 2021!"*

**YE OLDE TABLE OF CONTENTS**

1. **Introduction** *Wherein is answered the question of what it is and what it's for*
3. **Installation** *Wherein is answered the question of how to make it go*
2. **Documentation by Examples** *Wherein is answered the question of how to use it*
4. **Hacking** *Wherein is -- oh, this is getting boring*

## Introduction

*or, What is it? and what's it for?*

Piltdown is a tiny, nay, even trivial Python library
that generates Unicode strings of bar charts
and some other data visualization thingies
which are meant to be included in your Twitter posts.

See the Documentation section below for examples.

What kind of charts, you ask? Also see the Documentation section for examples.

But see all the caveats.
I mean, they're pretty obvious.
There is only so much you can do with nothing but text
that is always left-justified,
displayed in a very narrow column,
and in a variable-width font--
even with Unicode.
If you think you can pull off a scatter plot with variable width Unicode in the space of a tweet, by all means, send me a PR.

I wrote this for the fun of it,
on a lark. Don't get all testy with me.

### The Basic Idea

For most of the types of plot, you will specify your data set,
(typically a list, list of tuples, dict, etc.).
Generating this from a datafrane or other form is your problem--Piltdown just generates strings. That's all.
There are a million utilities that could be included
to post your string to Twitter for you,
or to do other Unicode tricks,
like bold or italics,
but at least for the moment
Piltdown wants to do one thing and do it (tollerably) well:
generate strings that work as data viz in the space of a tweet.
That means generally just the graphic elements and sometimes axis labels.
Titles and keys are mostly your problem.
But the idea is that all you have to do is concatenate any string you want
with the output of your Piltdown graph,
and thus becometh Robert your parent's brother.


## Installation

Clone the repository and do 

    pip install .
    
or the local equivalent (eg. pip3 install . )

Or at some point maybe I will make it installable from PyPi or whatever it is.

Or you can just, like, load up the files any old way you want. It's pretty simple.

Anyway, if you do the pip thing, then import things as you need them as per the examples in, you guessed it, the Documentation section below.


## Documentation by Example, or Ye Olde Plots

In alphabetical order:

 - Horizontal Dot Chart

### Horizontal Dot Chart

Not to be confused with a dot plot.
This is the kind of thing they use on Khan Acadamy
to teach small children about data.
This is the horizontal version.

### Example

Note Labels are automatically converted to the Unicode manthimatical "fullwidth" characters, which do not play nicely with screen readers. Beware the righteous wrath of the screen reader user.


```python
import piltdown.hdot_chart as hdot

print(
    "How many times I ate chocolate this week:\n\n"
    + hdot.hdot_chart(
        [3, 2, 4, 0, 2, 1, 4], ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    )
)

```

    How many times I ate chocolate this week:
    
    Ｍｏ:⚫⚫⚫
    Ｔｕ:⚫⚫
    Ｗｅ:⚫⚫⚫⚫
    Ｔｈ:
    Ｆｒ:⚫⚫
    Ｓａ:⚫
    Ｓｕ:⚫⚫⚫⚫


## Hacking

#### Project goals

- Simple
- Really simple
- Simple enough to just write static documentation here
- Simple enough that the examples in the documentation here can be the test suite
- Don't try to do anything but create the charts and graphs.
  Just functions that return strings.
  Leave Twitter posting, statistical preprocessing,
  and mixing output with other strings (titles, general writing, etc.)
  to the user/other libraries.
- Easy to use.
- Just focused on the Twitter use case.
  Not a general solution to the grand ASCII-art Data Viz Problem,
  which is never-ending.
  
#### And also

The README is generated from this Jupyter notebook. Don't forget to re-export it to README.md if you make changes.

#### TODO

- Well, yeah, maybe I do want to do bold and italic fonts as a utility function. Also maybe some variables bound to generally useful Unicode characters (smileys, Harvey balls, etc)

A list of plots I got somewhere that looked at a quick glance like they might be possible. Not to be interpreted as firm intentions:

- horiz bar
- heatmap
- stacked bar
- boxplot
- column sparkline
- win/loss sparkline
- treemap
- matrix diagram
- pictorial fracrion
- horiz hist
- waffle
- funnel
- linear process diag
- grouped bar
- nested/layered proportional area
- pictorial unit
- dot plot
- pyramid diag
- dumbell plot
- bullet diag
- partition layer chart icicle diag
- stepped line graph
- scaled up number
- lollypop chart
- comparison chart
- kagi chart
- dot matix
- pictogram
- stem and leaf 



```python

```
