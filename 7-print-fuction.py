"""
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that ... represents the values in between.
"""
from __future__ import print_function
def print_function(n):
    for i in range(1, n + 1):
        print (i, end=''),

n = int(raw_input())

print_function(n)
