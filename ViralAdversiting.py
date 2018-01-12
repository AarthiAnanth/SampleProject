
n = int(input())
total=0
m=5
liked=0
shared=0
while n!=0:
    liked=m//2
    shared=liked*3
    total+=liked
    m=shared
    n-=1
print(total)   
    