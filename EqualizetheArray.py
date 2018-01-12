n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
temp=[]
count=0
for i in c:
    if i not in temp:
        temp.append(i)
max=0
x=0
for j in temp:
    if c.count(j)>max:
        max=c.count(j)
        x=j
for y in c:
    if y!=x:
        count+=1
print(count)
