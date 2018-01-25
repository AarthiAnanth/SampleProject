import sys

def pangram(s):
    list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    p=s.lower()
    count=0
    for i in list1:
        if i in p:
            count+=1
    if count==26:
        return 'pangram'
    else:
        return 'not pangram'
        

s = input().strip()
result = pangram(s)
print(result)