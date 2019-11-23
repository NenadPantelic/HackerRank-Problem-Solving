#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    count = 0
    if (n == 1 and m == 1):
        return int(s[0] == d)
    for i in range(n-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

