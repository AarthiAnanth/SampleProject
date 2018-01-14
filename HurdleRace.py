#!/bin/python3

import sys

def hurdleRace(k, height):
    # Complete this function
    if(k>max(height)):
        a=0
    elif(k<max(height)):
        a=(max(height)-k)
    return a

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
