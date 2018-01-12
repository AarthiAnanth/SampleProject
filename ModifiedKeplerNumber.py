p = int(input().strip())

q = int(input().strip())
square=0
half=0
left=""
right=""
list1=[]
sum=0
for i in range(p,q+1):
    if i<10:
        square=i*i
        if (square%10)+(square//10)==i:
            list1.append(i)
    elif i>=10:
        square=str(i*i)
        half=len(square)//2
        left=square[:half]
        right=square[half:]
        sum=int(left)+int(right)
        if sum==i:
            list1.append(i)
if len(list1)>0:
    for x in list1:
        print(x,end=" ")
else:
    print("INVALID RANGE")