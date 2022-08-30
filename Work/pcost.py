# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        try:
            stock = int(row[1]) * float(row[2])
            total = total + stock
        except ValueError:
            print('Warning missing field')
    f.close()
    return round(total, 2)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)


