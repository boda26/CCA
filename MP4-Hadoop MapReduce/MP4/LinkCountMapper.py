#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    line = line.split(": ")
    src, dsts = line[0], line[1].split()
    for d in dsts:
        output = src + '\t' + d
        print(output)
       
