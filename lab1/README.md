# Lab 1: Tools of the trade

## Part 1: Installing things

For this seminar you will need:
- Python - install using [Anaconda](https://www.anaconda.com/download/) (works for Mac, PC, Linux)
- GitHub account
- Git (can be installed on PC using the GitHub app)


## Part 2: Downloading/submitting materials for the seminar

The seminar will be a single open source repository, which lives on GitHub at:
https://github.com/jradavenport/WWU-seminar-2018 <br/>
Here's how each week will go:

1) You will need to "[Fork](https://help.github.com/articles/fork-a-repo/)" this repository (copy it) to your own GitHub account.

2) Then "[Clone](https://help.github.com/articles/cloning-a-repository/)" your version on to whatever machine you're using. You'll have to [configure your local version](https://help.github.com/articles/configuring-a-remote-for-a-fork/) to point back at the original source:

Each week a lab will appear in a new sub-directory, which will have example code and data files you'll need. You will have to [sync your fork](https://help.github.com/articles/syncing-a-fork/) with my original version each week!


3) Then, **do the assignment**. Either start a new Jupyter notebook, or duplicate the example notebook. **Don't just modify the example and turn it in!** Good practice: create a new notebook with name `lab1-LASTNAME.ipynb`.

4) To turn in your assignment: **Commit** your changes to your local "repo", **push** back to your fork on GitHub. Finally, on GitHub [submit a pull request](https://help.github.com/articles/using-pull-requests/) back to the original (my) repo.

This process is confusing, and it took me a long while to memorize.


## Part 3: A simple calculation

Look at the example Notebook (`lab1-example.ipynb`) file in the Lab1 directory. If you view it on GitHub, you'll notice it is rendered nicely in the browser. Sweet! However, this is just a snapshot of the notebook when I synced it, and you cannot edit/run it unless you download it.

So, get the tools installed from Part 1, go through the steps in Part 2, and fire up the Jupyter Notebook locally. Usually on most machines you do this from the terminal (or shell) like this:

    jupyter notebook

But if you're using the Anaconda "Launcher", or similar, you might have an icon to click on.

The goal of this exercise is:
1. refresh your memory on how to use Python and Jupyter Notebooks
2. start getting comfortable with submitting assignments using GitHub
3. compute the radius that encloses half the mass of the Earth (total mass of the Earth is about `5.9e24 kg`)

There are many ways to solve this computational problem using the data that I've provided. You could do a FOR loop (as I've started to outline in the example notebook), you could make clever use of the numpy cumulative sum function...
