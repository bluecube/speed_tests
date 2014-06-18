#!/usr/bin/python3

import timeit
import random
import itertools
import operator

long_list = [random.randint(0, 1000) for i in range(10000)]
short_list = [random.randint(0, 1000) for i in range(100)]

def testit(what):
    print("testing {} - long list:".format(what))
    print(timeit.repeat(
        'list({}(long_list))'.format(what),
        'from __main__ import long_list, {0}'.format(what),
        number=1000
    ))
    print("testing {} - short list:".format(what))
    print(timeit.repeat(
        'list({}(short_list))'.format(what),
        'from __main__ import short_list, {0}'.format(what),
        number=1000000
    ))

def generator(sequence):
    it = iter(sorted(sequence))
    previous = next(it)
    for x in it:
        if x != previous:
            yield previous
            previous = x
    yield previous
testit('generator')

def groupby1(sequence):
    return (x[0] for x in itertools.groupby(sorted(sequence)))
testit('groupby1')

def groupby2(sequence):
    return map(
        operator.itemgetter(0),
        itertools.groupby(sorted(sequence)))
testit('groupby2')

def sorted_set(sequence):
    return sorted(set(sequence))
testit('sorted_set')

# Too slow
#def uniq_zip(sequence):
#    yield sequence[0]
#    yield from (x for prev, x in zip(sequence[:-1], sequence[1:]) if prev != zip)
# testit('uniq_zip')
