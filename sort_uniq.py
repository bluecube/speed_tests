#!/usr/bin/python3

import timeit
import random
import itertools
import operator

data = sorted(random.randint(0, 1000) for i in range(100000))

def testit(what):
    print("testing {}:".format(what))
    print(timeit.repeat(
        'list({}(data))'.format(what),
        'from __main__ import data, {0}'.format(what),
        number=1000
    ))

def generator(sequence):
    it = iter(sequence)
    previous = next(it)
    for x in it:
        if x != previous:
            yield previous
            previous = x
    yield previous
testit('generator')

def groupby1(sequence):
    return (x[0] for x in itertools.groupby(sequence))
testit('groupby1')

def groupby2(sequence):
    return map(
        operator.itemgetter(0),
        itertools.groupby(sequence))
testit('groupby2')

# Too slow
#def uniq_zip(sequence):
#    yield sequence[0]
#    yield from (x for prev, x in zip(sequence[:-1], sequence[1:]) if prev != zip)
# testit('uniq_zip')
