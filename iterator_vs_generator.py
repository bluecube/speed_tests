#!/usr/bin/python3

import timeit

def testit(what):
    print("testing {}:".format(what))
    print(timeit.repeat(
        'sum({0}())'.format(what),
        'from __main__ import {0}'.format(what)
    ))

class Iterator:
    def __init__(self):
        self.x = 0
    def __next__(self):
        if self.x < 100:
            self.x += 1
            return self.x
        else:
            raise StopIteration()

    def __iter__(self):
        return self

def generator():
    x = 0
    while x < 100:
        x += 1
        yield x

testit('Iterator')
testit('generator')
