import numpy as np
import pandas as pd


def constell_davenport(x,y):
    '''
    Determine which constellation a set of coordinates is located in.
    Based on the algorithm from N. G. Roman 1987, PASP, 99, 695. Written by @jradavenport

    This version uses Numpy arrays, and can operate on either a single (x,y) coordinate,
    or a list of coordinates.

    Parameters
    ----------
    x : float or float array
        Right Ascension (RA) of target, in decimal hours in the range [0, 24]
    y : float or float array
        Declination (Dec) of target, in decimal degrees in the range [-90, 90]

    Returns
    -------
    string or string array
        Abbreviation of constellation for each set of coordinates
    '''

    # read the data in every time (runtime overhead....)
    df = pd.read_csv('../lab2/data/data.csv')

    # handle lists of coordinates
    if np.size(x) > 1:
        outname = []

        for k in range(np.size(x)):

            c1 = np.where((df['DE_low'].values <= y[k]))

            c2 = np.where((df['RA_up'].values[c1] > x[k]))

            c3 = np.where((df['RA_low'].values[c1][c2] <= x[k]))

            outname = np.append(outname, df['name'].values[c1][c2][c3][0])

        return outname

    # handle old-fashioned single coordinate case
    else:
        c1 = np.where((df['DE_low'].values <= y))

        c2 = np.where((df['RA_up'].values[c1] > x))

        c3 = np.where((df['RA_low'].values[c1][c2] <= x))

        return df['name'].values[c1][c2][c3][0]


def constell_scoggins(ra,dec):

    '''
    This is a function to find a constellation based on right-ascension and declination angles
    Written by @mscoggs

    Parameters
    ----------
    arg1 : float
        right ascension
    arg2 : flaot
        declination

    Returns
    -------
    string
        associated constellation
    '''

    df = pd.read_csv('../lab2/data/data.csv')

    for x in range(358):
        if df['DE_low'][x] < dec:
            for y in range(x, 358):
                if df['RA_up'][y] > ra:
                    for z in range(y, 358):
                        if ((df['RA_low'][z] < ra) & (df['RA_up'][z]>ra)):
                            return (df['name'][z])
