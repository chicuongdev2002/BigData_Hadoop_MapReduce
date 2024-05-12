#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns based on comma (assuming CSV format)
    columns = line.split(',')
    # check if the line has expected number of columns
    if len(columns) == 8:
        # extract genre and price before tax
        genre = columns[1].strip()
        priceex = float(columns[3])
        # output genre as key and priceex as value
        print '%s\t%s' % (genre, priceex)
