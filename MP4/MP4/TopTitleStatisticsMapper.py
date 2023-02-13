#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    line = line.split('\t')
    ct = line[1]
    print(ct)
    # print('%s\t%s' % (  ,  )) pass this output to reducer
