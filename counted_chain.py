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
it = {0}(iterators())
        '''.format(what)
    ))

chain_from_iterable = itertools.chain.from_iterable
testit('chain_from_iterable')

def manual_counting(slaves_it):
    i = 0
    for slave in slaves_it:
        for sample in slave:
            yield sample
            i += 1
testit('manual_counting')

def top_level_count(slaves_it):
    samples_it = iter([])
    for i in itertools.count():
        while True:
            try:
                yield next(samples_it)
            except StopIteration:
                samples_it = iter(next(slaves_it))
            else:
                break
testit('top_level_count')

def top_level_count_no_empty(slaves_it):
    samples_it = iter([])
    for i in itertools.count():
        try:
            yield next(samples_it)
        except StopIteration:
            samples_it = iter(next(slaves_it))
            yield next(samples_it)
testit('top_level_count_no_empty')

