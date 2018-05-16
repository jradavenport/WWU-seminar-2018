# Lab 6: Monte Carlo Simulations

Today we're going to reproduce a classic experiment, and in the process learn a very useful technique for doing simulations with a computer. *Note this may overlap concepts you've learned in numerical physics courses, but we'll use it as an excuse to learn more Python skills!* We'll be exploring a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) problem, which I tend to think about as "dice rolling" problems. This technique is incredibly valuable in Astronomy, where we can have physical situations or  equations that are impossible empirically solve. Instead we simplify the problem, and let the computer tell us the "normal" answer.


## Buffon's needle
The experiment we're going to simulate is called [Buffon's Needle](https://en.wikipedia.org/wiki/Buffon%27s_needle). In this experiment we are going to drop a needle with length `l` onto a floor that is covered in infinitely long parallel lines spaced at a distance `d`. For simplicity, let's further assume that the needle is the same length as the line separation, so `l = d`.

**The goal** is to "drop" the needle randomly `N` times on this infinite floor, and count how often it intersects one of the parallel lines.


## Approaching the problem
To create a "simulation" of this physical scenario, we have to decide what the physical parameters to model are. The floor is simple: it is infinite, with lines evenly spaced along (say) the Y-axis, and we can assume the first line crosses `Y=0`.

For the needle, at each drop we need to model:
- The center position of the needle in `(X,Y)` space
- The angle of the needle

You could generate this model using (uniform) random numbers scaled to the domain of each variable. For example, the angle is a random number in the range [0, 360] deg.


## Simplifying the problem
- Since the floor is infinite in the Y-direction, we can ignore the Y-axis position of the needle.
- Since the floor is also infinite in the X-direction, we can divide the X-axis by `d`, and only simulate the needle landing in the range [0, 1].

Now, given the X position and angle of the needle for each drop, you must figure out IF the needle crosses either `X=0` or `X=1`.


## Output
- Write this simulation as a function that takes `N` as an argument, and perhaps `l` and `d` as kwargs (with default values of 1). Use Numpy arrays and random number generators.
- Have your function output an array of either True/False or 0/1 with length `N`
- Do your simulation for `N=[1, 10, 1e3, 1e6]`
- After each run of your simulation, compute `P = 2 N / n`, where `n` is the number of line crossings (True's), and `N` is the number of throws.

**BONUS:** For the 1e6 trials case, make a plot of `P(N)` as the number of trials increases to 1e6. You should see `P` converge to a natural constant as you increase `N`
