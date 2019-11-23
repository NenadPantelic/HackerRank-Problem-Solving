
#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    socks = dict([val,0] for val in ar)
    for sock in socks:
        socks[sock] = ar.count(sock)
    return sum(list(map(lambda s:s//2,list(socks.values()))))
        
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

