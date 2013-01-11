#!/usr/bin/env python

import random

count = 10000

for i in xrange(count):

    print '13' + ''.join(['%s'% random.randint(0, 9) for _ in xrange(9)])
