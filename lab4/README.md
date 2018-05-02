# Lab 4: Data Wrangling, File Input/Output

Ask any programmer, scientist, or data analyst: one of the most frustrating parts of research is dealing with other people's data. Today we'll look at a few helpful tools to read in data, and a couple ways to write it too.

Python official documentation on the subject is [here](https://docs.python.org/3.3/tutorial/inputoutput.html)

## Part 1: Update your Fork

Just like last week, you have to update the Fork to include the new lab! So, once again: [sync the latest revisions into your Fork](https://help.github.com/articles/syncing-a-fork/).

(By the way: a brute force way to do this is to delete your fork and your local clone, and re-fork it and clone it from scratch. This is a good workaround when things get very messed up...)



## Part 2: Reading Files

**Note:** these examples are pretty *easy*, in that they don't have large portions of missing data, binary data files (e.g. Pickle or save files), weird structured data (e.g. XML files), or highly unique formats (e.g. HEALpix or HDF5). You will encounter strange formats. The way to succeed is to **beg/borrow/steal** solutions to get the data to read (i.e. Google/StackOverflow). Python has a way to read almost any data you could possibly want!

I have pushed you towards using Pandas in this seminar, primarily because it makes reading (and writing) many types of files easy and uniform.


**TIP 1:** Microsoft Excel, for all its shortcomings, is one of the most advanced data wrangling environments ever built. There's nothing wrong with opening your datafile in Excel, rearranging it, and then exporting it to something Python can read (e.g. a .csv file).


**Tip 2:** If there are strange values, weird delimiters, missing data, extra spaces... you can sometimes just open files in TextEdit/NotePad/[Atom](https://atom.io/) and do a search & replace.


### 2.1: Read a simple text file
We've done this before, using simple .csv files (e.g. [Lab 1](https://github.com/jradavenport/WWU-seminar-2018/tree/master/lab1)) with `pd.read_csv`. This is an important basic tool!
- Now try reading in another simple text file using the similar `pd.read_table`
- The file is: `data/2mass_photometry.tbl`, It contains data from the 2MASS database.


### 2.2: Make a plot with this data
Make a plot of the infrared *color magnitude diagram*, i.e. (J-K, J) for this field
- remember, flip the Y-axis for magnitudes! (silly astronomers)
- Highlight (use different color, points, etc) stars within 0.25 deg from the field center (RA=132.825deg, Dec=11.80deg)
- This is the famous open cluster [M67](https://en.wikipedia.org/wiki/Messier_67)



### 2.3: Read an astronomy image (FITS file)
- FITS stands for Flexible Image Transport System, the long standing default in astronomy
- You may see `.fits` and `.fit` files interchangeably
- Need a special reader to parse them. In Python, the standard is part of astropy: `astropy.io.fits`
- Reading it creates an "astropy table", which is very similar to a Pandas dataframe (in fact, you can convert to a dataframe!)
- Make a plot of the light curve using the columns: (time, PDCsap_flux)
- Can you spot the transiting exoplanet, Kepler 7b? Neat!
- **Bonus:** When was this image taken? Get data from the Header!


## Part 3 Writing Files

### 3.1: Save the image of the planetary nebula to a new file
- use a .png extension (the default)
- Try a .pdf extension. Python/Matplotlib is smart and knows how to write many
file types!


### 3.2: Save some numeric data to an output file
- There are a lot of ways to save output data
- What's most important is that you remember what data is in which column. I suggest using headers or named columns when possible! "Pythonic" code (and data) is readable!
- Select stars where their coordinates are within a radius of 0.25deg of the field center (as in the first plot)
- Center: RA=132.825deg, Dec=11.80deg
    - Save JUST these stars to an output text file
- I suggest CSV for ease of reading.
    - I suggest trying to use Pandas for this!
- make a new DataFrame using only the columns you need
- select only the stars within 0.25deg of field center
- use the `.to_csv()` method to output it.
