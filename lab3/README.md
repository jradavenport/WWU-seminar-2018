# Lab 3: Algorithm 2: Break Your Code!

The goal today is to learn about testing your code. Good software is written with "unit tests" in mind, which are basic conditions the code must meet every time it is run. Think of these like boundary conditions (e.g. the mass of the Earth from Lab 1 had better be close to the known value), or limiting cases (e.g. "What happens when I enter a zero into the algorithm?"). Writing good tests will ensue that your code works for all possible use cases, and means it's less likely to break when somebody else tries to use it!

Tests can also measure the performance of your code/algorithm. This is very important when you need to run code on a massive dataset, or are putting a job on an expensive supercomputer and need to get answers as quickly (cheaply) as possible.

The best thing to do is write a series of these basic tests that your code must pass, so today that's what we're going to do!



## Part 1: Update your Fork

Just like last week, you have to update the Fork to include the new lab! So, once again: [sync the latest revisions into your Fork](https://help.github.com/articles/syncing-a-fork/).

(By the way: a brute force way to do this is to delete your fork and your local clone, and re-fork it and clone it from scratch. This is a good workaround when things get very messed up...)



## Part 2: SPEED RACER

We'e going to use solutions from the Constellation Algorithm from last week. There are 2 solutions in the `solutions.py` file I have provided.

### 2.1: If you have a solution from last week
    - add it to the `solutions.py` file!
    - If not, just use what is provided
