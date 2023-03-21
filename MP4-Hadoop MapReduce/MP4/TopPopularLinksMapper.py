#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    l = line.split('\t')
    output = l[0] + '\t' + l[1]
    print(output)
