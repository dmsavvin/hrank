'''
See exercise description at
https://www.hackerrank.com/challenges/summing-pieces/problem
'''


def summing_pieces(arr):
    D = 10 ** 9 + 7
    n = len(arr)
    c = (pow(2, n, D) - 1) % D
    v = (arr[0] * c) % D
    for i in range(2, n + 1):
        c = (c + pow(2, n - i, D) - pow(2, i - 2, D)) % D
        v = (v + arr[i - 1] * c) % D
    return v
