# report.py
#
# Exercise 2.4

import csv


def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for name, shares, price in rows:
            holding = {'name': name,  'shares': int(shares), 'price': float(price)}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    portfolio = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                dic = {row[0]: float(row[1])}
                portfolio.update(dic)
            except IndexError:
                pass
    return portfolio


def show_portfolio(filename):
    print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s}')
    print(f'{"----------":>s} {"----------":>s} {"----------":>s}')
    portfolio = read_portfolio(filename)
    # for row in portfolio:


show_portfolio('Data/portfolio.csv')


























