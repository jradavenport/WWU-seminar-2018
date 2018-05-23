# Lab 7: Fitting Models to Data

"Fitting a model" can be a simple as drawing a line through some data points, and as complicated as requiring years of computing time on a supercomputer. Model fitting is at the very heart of science, and is the critical stage where we decide if our observations match our theoretical expectations.

A huge amount of literature is available on this subject. For example, I enjoy this [book chapter](https://arxiv.org/abs/1008.4686) by D. Hogg, and you can find [recorded videos](https://www.youtube.com/watch?v=0tYaMTK-1K0) of him giving these lectures. An incredible tool for fitting data and exploring models is `emcee`, a "[MCMC](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)" package that has been used to [do some of the exact examples](http://dfm.io/emcee/current/user/line/) that Hogg discusses.
There are also some great [blog posts](http://jakevdp.github.io/blog/2015/08/07/frequentism-and-bayesianism-5-model-selection/) and videos ([here](https://www.youtube.com/watch?v=ljBhVbJ0QHU) and [here](https://www.youtube.com/watch?v=NvSgyWmb5Hk)) by J. VanderPlas that I would suggest looking at.

Today we'll ignore much of the important details, and instead focus on demonstrating some of the **most basic** approaches to getting lines/curves to go through the data.

The example notebook is more robust than previously, and has instructions in it. I'll briefly describe our 2 goals for today here:

## 1. Fit basic lines to Supernovae data

- We're examining a catalog of SNe, compiled from HST, Gemini, and VLT by [Amanullah et al. (2010)](https://arxiv.org/abs/1004.1711)
- The diagram we wish to make is the [distance modulus](https://en.wikipedia.org/wiki/Distance_modulus) vs redshift (z, mu) diagram. This reproduces their Figure 9
- This diagram is also known as a "[Hubble Diagram](http://www.pnas.org/content/101/1/8)"

**BONUS:**
- Convert the distance modulus into Mpc (mega-parsecs)
- Convert the redshift into redshift velocity
- The slope of the new fit is actually [Hubble's Constant](https://en.wikipedia.org/wiki/Hubble%27s_law#Observed_values_of_the_Hubble_constant)!
    - has units of `(km/s)/Mpc`, so you may need to invert your fit to get the right number.


## 2. Fit a spectral emission line using a Gaussian curve

- We're using a high redshift (very distant) [quasar](https://en.wikipedia.org/wiki/Quasar). This is an "active" galaxy, and we're going to estimate it's [redshift](https://en.wikipedia.org/wiki/Redshift#Measurement,_characterization,_and_interpretation).
- This is a chance to work with a spectrum from the famous [Sloan Digital Sky Survey](http://www.sdss.org), now in it's 14th data release!
- Fit the emission line centered around (observed) wavelength of 5610 Angstroms. That is the Mg II emission line, whose rest wavelength is 2800.3 Angstroms.
