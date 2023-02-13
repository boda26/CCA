#!/usr/bin/env python3
import sys

words = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    w = line.split('\t')
    words.append(w)

words.sort(key=lambda w: (int(w[1]), w[0]))

for w in words[-10:]:
    output = w[0] + '\t' + w[1]
    print(output)

# print('%s\t%s' % (  ,  )) print as final output