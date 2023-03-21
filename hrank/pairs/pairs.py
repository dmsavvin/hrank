'''
See exercise description at
https://www.hackerrank.com/challenges/pairs/problem
'''


def pairs(k: int, arr: list) -> int:
    n = len(arr)
    arr.sort()
    res = 0
    begin = 0
    end = 0
    while begin < n and end < n:
        if arr[end] - arr[begin] == k:
            res += 1
            begin += 1
            end += 1
            continue
        if arr[end] - arr[begin] < k:
            end += 1
            continue
        if arr[end] - arr[begin] > k:
            begin += 1
            continue
    return res
