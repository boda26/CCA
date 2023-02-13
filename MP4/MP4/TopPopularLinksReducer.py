#!/usr/bin/env python3
import sys

links = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    l = line.split('\t')
    links.append(l)

links.sort(key=lambda l: (int(l[1]), int(l[0])))

for l in links[-10:]:
    output = l[0] + '\t' + l[1]
    print(output)
