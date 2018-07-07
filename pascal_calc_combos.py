#!/usr/bin/env python3

import functools


inputn = input("How many ingredients are there? :")
inputk = input("How many ingredients are you allowed to put on your pizza? :")
n = int(inputn)+1
k = int(inputk)


def nCk(n, k):
    return functools.reduce(
        lambda x, y: x * y[0] / y[1],
        zip(range(n - k + 1, n+1), range(1, k+1)), 1
        )

number = (nCk(n-1, k))
fnumber = format(number).rstrip('0').rstrip('.')


def gen_pascal(n):
    k = []
    for x in range(n):
        l = len(k)
        k = [1 if i == 0 or i == l else k[i-1]+k[i] for i in range(l+1)]
        yield k


def draw_triangle(n):
    ps = list(gen_pascal(n))
    max = len(' '.join(map(str, ps[-1])))
    for p in ps:
        print(' '.join(map(str, p)).center(max))

draw_triangle(n)

print(
    '\n' +
    'There are exactly ' +
    fnumber +
    ' different possible combinations of pizza you could make!'
    )
