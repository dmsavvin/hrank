'''
See exercise description at
https://www.hackerrank.com/challenges/stockmax/problem
'''


def stockmax(prices):
    profit = 0
    n = len(prices)
    maxs = [0]
    for p in prices[::-1]:
        maxs = [max(p, maxs[0])] + maxs
    for i in range(n - 1, -1, -1):
        profit += max(maxs[i] - prices[i], 0)
    return profit
