# Lab 3: Algorithm 2: Break Your Code!

The goal today is to learn about testing your code. Good software is written with "unit tests" in mind, which are basic conditions the code must meet every time it is run. Think of these like boundary conditions (e.g. the mass of the Earth from Lab 1 ought to be close to the known value), or limiting cases (e.g. "What happens when I enter a zero into the algorithm?"). Writing good tests will ensue that your code works for all possible use cases, and means it's less likely to break when somebody else tries to use it!

Tests can also measure the performance of your code/algorithm. This is very important when you need to run code on a massive dataset, or are putting a job on an expensive supercomputer and need to get answers as quickly (cheaply) as possible.

The best thing to do is write a series of these basic tests that your code must pass, so today that's what we're going to do!



## Part 1: Update your Fork

Just like last week, you have to update the Fork to include the new lab! So, once again: [sync the latest revisions into your Fork](https://help.github.com/articles/syncing-a-fork/).

(By the way: a brute force way to do this is to delete your fork and your local clone, and re-fork it and clone it from scratch. This is a good workaround when things get very messed up...)



## Part 2: SPEED RACER

We're going to use various solutions from the Constellation Algorithm from last week, and see how fast each is as we add more and more coordinates to test.

### 2.1: Use the previous solutions
    - There are 2 solutions in the `solutions.py` file I have provided.
    - If you have a solution of your own, add it to the `solutions.py` file!
    - If not, just use what is provided

### 2.2: Write a function to test the speed of the 2 (or 3) constellation algorithms.
 - This function should take `N` as the input argument (the number of coordinates to test),
 - The function must generate `N` random coordinates (both RA and Dec), pass these to the algorithms, and measure the time it takes each
 - The function should return 2 (or 3) runtimes.
 - **Note:** the Davenport code can accept arrays of coordinates as a single input, and the Scoggins code cannot... you'll need to wrap it in a loop

### 2.3: Plot the performance as a function of N for the 2 (or 3) algorithms
You'll need to save the outputs for each `N`. Maybe do a `for` loop over a range of `N` values? Explore the speed of each algorithm between  `N=1` and `N=10000` (note you *don't have to* try every `N` between them...)

How efficient are the algorithms? Do they do better in different regimes? Do they "flatten" or does runtime keep increasing with larger `N`?

**Bonus:** Look at the algorithms and think about WHY they behave the way they do?



## Part 3: Tests

Finally today we'd like to generate some basic tests of the algorithm! We want to check that our algorithm is working correctly. We'll do this by comparing answers.

### 3.1: Write a test function
Create a VERY SIMPLE function that takes 3 arguments (ra, dec, constellation), and returns a `True` or `False` if the given (ra,dec) is within that constellation. Demonstrate this using the coordinates from last week.

### 3.2: Test at scale!
Write a wrapper function that steps through all of the "Named Stars" (the new data provided this week). For each star, compute it's constellation based on the coordinates (RA, DEC), and test that to the official constellation designation.

Does your code get them all correct? (*Hint:* Mine doesn't for about 16 objects, and yours likely won't either!)

Tips:
- since the two datasets we're using type the constellation abbreviations differently, you should convert them both to *lowercase* (or uppercase). I do this with a `.lower` after each (example in notebook)
- print out *which* stars fail. Compare w/ your friends!

Why do you think these stars failed?
