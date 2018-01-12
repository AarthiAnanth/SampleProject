i,j,k= input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]
if i<j:
    count=0
    for x in range(i,j+1):
        sub=0
        string=str(x)
        string=string[::-1]
        sub=x-int(string)
        if sub%k==0:
            count+=1
    print(count)
            