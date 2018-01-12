def function(n,l):
    level=0
    valley=0
    for i in l:
        for j in i:
            if j=='U':
                level+=1
            elif j=='D':
                if level==0:
                    valley+=1
                level-=1
            
    print(valley)

n=int(input().strip())
l=list(map(str,input().strip().split(' ')))
result=function(n,l)