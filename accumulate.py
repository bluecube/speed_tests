#!/usr/bin/python3

import timeit
import itertools

def iterators():
    while True:
        yield iter(range(1000))

def testit(what):
    print("testing {}:".format(what))
    print(timeit.repeat(
        'next(it)',
        '''
from __main__ import iterators, {0}
import itertools
it = {0}(itertools.count(), 0.15, 0.1)
        '''.format(what)
    ))

def cumsum(it, add, multiplier):
    """
    Calculate cumulative sum of it, modifying each result
    using linear function.
    """
    accumulator = add
    for x in it:
        yield multiplier * accumulator
        accumulator += x
testit('cumsum')

def accumulate_with_wrapper(a, b, c):
    return (x * c + b for x in itertools.accumulate(a))
testit('accumulate_with_wrapper')


##########################################################################

def testit2(what):
    print("testing {}:".format(what))
    print(timeit.repeat(
        'next(it)',
        '''
from __main__ import iterators, {0}
import itertools
it = {0}(itertools.count(), itertools.count(), 0.1)
        '''.format(what)
    ))

def cumsum2(it, add_it, multiplier):
    """
    Calculate cumulative sum of it, modifying each result
    using linear function.
    Add is an iterator.
    """
    accumulator = 0
    for x, add in zip(it, add_iter):
        yield multiplier * accumulator + add
        accumulator += x
testit2('cumsum2')

def accumulate_with_wrapper(a, b, c):
    return (x * c + bb for x, bb in zip(itertools.accumulate(a), b))
testit('accumulate_with_wrapper')

