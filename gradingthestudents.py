#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in grades:
        if i>=38:
            a=i
            while i%5!=0:
                i+=1
            if((i-a)<3):
                print(i)
            else:
                print(a)
        else:
            print(i)
            
            

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


