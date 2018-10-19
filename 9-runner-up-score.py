"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n.
The second line n contains an array A[]  of n integers each separated by a space.

"""
n = int(raw_input())
arr = map(int, raw_input().split())
# after that we receive list, not the arr
arr.sort()
arr.reverse()
print arr
i = 0
while i < len(arr):
    if arr[i] != arr[i+1]:
        print arr[i+1]
        break
    else:
        i += 1



