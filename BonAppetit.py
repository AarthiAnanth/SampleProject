n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
b=int(input())
sum=0
for i in range(n):
    if i!=k:
        sum+=c[i]
if sum//2==b:
    print('Bon Appetit')
else:
    if b>sum//2:
        print(b-(sum//2))
    elif sum//2>b:
        print((sum//2)-b)
        
