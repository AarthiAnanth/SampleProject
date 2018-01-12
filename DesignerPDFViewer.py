#!/bin/python3

import sys
def function(h,word):
    string='abcdefghijklmnopqrstuvwxyz'
    list1=[]
    for i in string:
        list1.append(i)
    max=0
    for i in range(len(list1)):
        for j in word:
            if j==list1[i]:
                if max<h[i]:
                    max=h[i]
    return max*(len(word)*1)
                
        
    

h = list(map(int, input().strip().split(' ')))
word = input().strip()
print(function(h,word))