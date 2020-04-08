import sys


def indianJob(g, arr):
    t = 0
    i = len(arr)-1
    arr.sort()
    vault = []
    if arr[-1] > g:
        return "NO"
    while i >= 0:
        robber1 = arr[i] + t
        vault.append(robber1)
        i -= 1
        #count += 1
        if len(vault) < 2:
            if i >= 0:
                robber2 = arr[i] + t
                vault.append(robber2)
                i -= 1
        t = min(vault)
        if vault[1] == t:
            vault.pop(1)
        if vault[0] == t:
            vault.pop(0)
            
        if t == g:
            if i == -1 and len(vault) == 0:
                return "YES"
            return "NO"
        if t > g:
            return "NO"
    return "YES"
        
def indianJob(g, arr):
    t1 = g
    t2 = g
    arr.sort()
    if arr[-1] > g:
        return "NO"
    i = len(arr)-1
    while i >= 0:
        rob1 = arr[i]
        i -= 1
        # if i >= 0:
        #     rob2 = arr[i]
        #     i -= 1
        if t1 > t2:
            t1 -= rob1
        else:
            t2 -= rob1
        if t1 < 0 or t2 < 0:
            return "NO"
        if t1 == 0 and t2 == 0:
            if i == -1:
                return "YES"
            return "NO"
    return "YES"
            
        

t = 20
f = open("input.txt","r")
for t_itr in range(t):
    #ng = input().split()
    ng = f.readline().split()

    n = int(ng[0])

    g = int(ng[1])

    arr = list(map(int, f.readline().rstrip().split()))

    result = indianJob(g,arr)

    print(result)


 

# # Test 1
# print(indianJob(4, [2,4,2]))        
# # Test 2
# print(indianJob(2, [2,4,3]))
# # Test 3
# print(indianJob(4, [2,2,3]))

# # Test 3
# print(indianJob(4, [2,2,2,2]))

# # Test 3
# print(indianJob(6, [5,2,1,4]))

# # Test 3
# print(indianJob(5, [5,2,1,4]))

        


