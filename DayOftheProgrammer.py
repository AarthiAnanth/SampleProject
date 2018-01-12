#!/bin/python3

import sys

def solve(year):
    result=""
    # Complete this function
    if year>1918:
        if (year%4==0 and year%100!=0) or year%400==0:
            date=256-(31+29+31+30+31+30+31+31)
        else:
            date=256-(31+28+31+30+31+30+31+31)
    elif year<1918:
        if year%4==0:
            date=256-(31+29+31+30+31+30+31+31)
        else:
            date=256-(31+28+31+30+31+30+31+31)
    elif year==1918:
        date=256-(31+28+31+30+31+30+31+31)+13
    return str(date)+'.09.'+str(year)
        
        
                

year = int(input().strip())
result = solve(year)
print(result)
