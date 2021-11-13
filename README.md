# footoe

A toy program that numbers foot-notes in 
a way I would prefer

### Motivation

I tired quickly of numbering foot-notes, in a text-file, myself.

If I had Foot-note Number 1 and Foot-note Number 2, and I suddenly
wanted to add a foot-note in between them, I had to make room for a new(er)
Foot-note Number 2. So I have to re-number the old(er) Foot-note
Number 2 to Foot-note Number 3. 

So, I thought, if I could give, to these foot-notes, any arbitrary 
number - or indeed, any alpha-numeric combination - how nice would it be if a program could
number these for me: starting from the number 1 to the final number that
represents the last foot-note in the text I have written.

### Elaboration

I want to do something like the way the Extended Syntax of Markdown 
handles foot-notes. An example can be seen 
[there](https://www.markdownguide.org/extended-syntax/#footnotes)

An expected input looks like the following:

```
Here's a foot-note,[^1] and here's another, longer, one.[^longnote]

[^1]: This is the first foot-note.

[^longnote]: This is the second foot-note.
```

And here is the expected output:

```
Here's a foot-note,[^1] and here's another longer one.[^2]

[^1]: This is the first foot-note.

[^2]: This is the second foot-note. 
```

Can you spot the difference?

### Installation

I assume you have Python set up, and optionally, Git Bash (if you are using the operating system Windows). 
Here is how you can operate the program in Windows:

0. Get a copy of the program. In your Git Bash (or similar), run: `git clone https://github.com/phtan/footoe.git`
0. Now open a Command Prompt instead of Git Bash
0. Navigate to the directory that you downloaded in Step 1 above. 
For example, by running: `cd footoe`
0. `python .\footoe\footoe.py -h`
