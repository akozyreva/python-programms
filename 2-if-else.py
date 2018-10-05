"""

Task
Given an integer, , perform the following conditional actions:

If n  is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

A single line containing a positive integer, n.
"""

n = int(raw_input("Type n: "))
if (n % 2 != 0) or (6 <= n <= 20):
    print "Weird"
else:
    print "Not Weird"
