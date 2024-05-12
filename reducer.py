#!/usr/bin/python

import sys

current_genre = None
max_price = float('-inf')

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    genre, priceex = line.split('\t', 1)
    # convert priceex (currently a string) to float
    try:
        priceex = float(priceex)
    except ValueError:
        # priceex was not a number, so silently ignore/discard this line
        continue
    # if the genre is the same, update the maximum price
    if current_genre == genre:
        max_price = max(max_price, priceex)
    else:
        # if this is a new genre, output the previous genre's maximum price
        if current_genre:
            print '%s\t%s' % (current_genre, max_price)
        # reset variables for the new genre
        current_genre = genre
        max_price = priceex

# output the maximum price for the last genre
if current_genre:
    print '%s\t%s' % (current_genre, max_price)
