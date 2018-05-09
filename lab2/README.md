# Lab 2: Algorithm 1: Do something!

Today we are thinking about algorithms, which is just a fancy word for "code that does a useful thing". This encompasses both the technical or mathematical challenge of solving problems, and the functional need for writing *well documented* code that works as expected.


## Part 0: Submit a Pull Request with last week's work

If you completed the lab from last week, feel free to [submit a pull request](https://help.github.com/articles/using-pull-requests/) back to the master version. A couple of you have (bravo!)

You could also submit one after you finish Lab 2, which includes your solution to both Lab 1 and Lab 2


## Part 1: Update your Fork

Recall: last week you "Forked" the master version of the Seminar repository on GitHub (then did the assignment and submitted a Pull Request). Now I've updated the project, and it's time for you to [sync the latest revisions into your Fork](https://help.github.com/articles/syncing-a-fork/).

So, add the upstream master to your local clone, and pull latest version *locally*. Your GitHub version will be synced too!

(By the way: a brute force way to do this is to delete your fork and your local clone, and re-fork it and clone it from scratch. This is a good workaround when things get very messed up...)


## Part 2: A basic "function"

One goal of writing useful computer code is to never repeat yourself, if possible. You achieve this by taking individual, repeatable tasks, and wrapping them up as "functions" (or classes, or methods, or what have you).


Some rules of the road:

- Python docs on [modules](https://docs.python.org/2/tutorial/modules.html)
- A function should perform a single task
- Every function should be completely documented, both "docstrings" and inline comments.
- Similar or related functions should be packaged together into modules
- In Python, use [classes](https://docs.python.org/2/tutorial/classes.html) to combine attributes and functions for "objects"
    - Won't discuss today, but very important.
- Python functions take "args" and "kwargs"...


### 2.1: Write a function called K2F that converts Kelvin to Fahrenheit

- Be sure to include all the required documentation
- Explore what happens when you give it unphysical values...
- Stretch goal: make the conversion go either way (F2K or K2F), using a flag/boolean

### 2.2: Put your function in a new file and import it into your IPython notebook (optional)
- Create a file called LASTNAME_func.py.
- Cut/Paste K2F in to it
- Then try importing and using your function in Python like:
````python
from LASTNAME_func import K2F
````
- Does it still work? (be sure K2F isn't defined elsewhere in the notebook!)
- Stretch goal: put another function in that same file. Switch your import statement to be more general:
````python
import LASTNAME_func as func
func.K2F
````


## Part 3: Constellation Algorithm

Today's real challenge is to implement the algorithm described by N. G. Roman 1987, PASP, 99, 695 (see handout). In the `data/`` directory I have included a data file you will find useful!


### 3.1: Implement the algorithm from Roman (1987)
- Skip "step 1", since we'll ignore precession.
    - Note, precession of stars from 1875 to today is significant! Like, ~30 arcmin...
- Use the provided data.csv file for Table 1
- Make this it's own method/function!
- What constellation does Vega lie in? (ra=18.62, dec=38.78)
- What constellation does HD 129078 lie in? (ra=14.78, dec=-79.03)
- Stretch goal: Plot the constellation boundaries and the location of the input star as part of your method.
