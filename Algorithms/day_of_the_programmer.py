#!/bin/python3

def solve(year):
    # Complete this function
    
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (year <= 1917 and year % 4 == 0):
        days[1] += 1
    elif year > 1917 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        days[1] += 1
    elif year == 1918:
        days[1] = 15
    datum = 256
    for i in range(len(days)):
        if datum <= 28:
            break
        datum -= days[i]


    
    month = str(i+1)
    if len(month) == 1:
        month = '0' + month
    return str(datum) + '.' + month + '.'+str(year)
   
        

year = int(input().strip())
result = solve(year)
print(result)


