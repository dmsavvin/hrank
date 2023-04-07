'''
See exercise description at
https://www.hackerrank.com/challenges/string-reduction/problem

Key idea is that if the original word can somehow be reduced to the 1 or 2 char
word we can stop searching and return 1 or 2 respectively. This is true because
if the original word can somehow be reduced to the word that is consisted of
the single char and has even/odd length there is no way to reduce original word
to odd/even length word which is consisted of the one char.

In other words if for a particular word the reduction process is terminated
with an even/odd length word it will always be terminated with an even/odd
length word for this original word.

Let us consider the following properties of the word:

Property 1: amount of every char in the word has the same parity (even or odd)
Property 2: there are chars in the word that have different parities

Those properties are invariants for the reduction process.
'''
import math


def get_children(word: str) -> set:
    children = set()
    for i, (ch_1, ch_2) in enumerate(zip(word[:-1], word[1:])):
        if ch_1 != ch_2:
            children.add(word[:i]
                         + (set('abc') - {ch_1, ch_2}).pop()
                         + word[i + 2:])
    return children


def string_reduction(word):
    global_min = math.inf
    if len(set(word)) == 1:
        return len(word)
    for child in get_children(word):
        local_min = string_reduction(child)
        if local_min < 3:
            return local_min
        global_min = min(global_min, local_min)
    return global_min
