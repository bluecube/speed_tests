#!/usr/bin/python3

import timeit
import numpy

vector = (1.2, 2.3, 3.4)
numpyvector = numpy.matrix([vector])

def testit(what):
    print("testing {}:".format(what))
    print(timeit.repeat(
        what,
        '''
import numpy
import math
from __main__ import vector, numpyvector'''))

print('vector =', repr(vector))
#testit('numpy.linalg.norm(vector)') # Too slow
testit('math.sqrt(sum(x*x for x in vector))')
testit('math.sqrt(math.fsum(x*x for x in vector))')
testit('math.sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])')

print()
print('numpyvector =', repr(numpyvector))

#testit('numpy.linalg.norm(numpyvector)') # Too slow
#testit('math.sqrt(numpy.sum(numpy.multiply(numpyvector, numpyvector)))') # Too slow
testit('math.sqrt(numpyvector * numpyvector.T)')
testit('math.sqrt(numpyvector[0,0] * numpyvector[0,0] + numpyvector[0,1] * numpyvector[0,1] + numpyvector[0,2] * numpyvector[0,2])')
testit('v = tuple(numpyvector.flat); math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])')
testit('v = numpyvector.flat; math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])')
testit('math.sqrt(math.fsum(x*x for x in numpyvector.flat))')
testit('math.sqrt(math.fsum(numpy.multiply(numpyvector.flat, numpyvector.flat)))')
