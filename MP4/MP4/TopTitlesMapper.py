#!/usr/bin/env python3
import sys

# TODO
words = []

for line in sys.stdin:
    #TODO
    line = line.rstrip('\n')
    w = line.split('\t')
    words.append(w)

words.sort(key=lambda w: (int(w[1]), w[0]))

for w in words[-10:]:
    output = w[0] + '\t' + w[1]
    print(output)


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
