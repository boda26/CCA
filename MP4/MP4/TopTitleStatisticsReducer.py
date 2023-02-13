#!/usr/bin/env python3
import sys
import math

#TODO

def find_mean(data):
    return sum(data) // len(data)

def find_var(data):
    var = 0
    mean = find_mean(data)
    for d in data:
        var += (d - mean)**2
    return var // len(data)

data = []

for line in sys.stdin:
    # TODO
    num = line.rstrip('\n')
    data.append(int(num))

mymean = find_mean(data)
mysum = sum(data)
mymin = min(data)
mymax = max(data)
myvar = find_var(data)

print(f'Mean\t{mymean}')
print(f'Sum\t{mysum}')
print(f'Min\t{mymin}')
print(f'Max\t{mymax}')
print(f'Var\t{myvar}')

#TODO
# print('%s\t%s' % (  ,  )) print as final output
