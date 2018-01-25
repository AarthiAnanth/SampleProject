
import sys

def marsExploration(s):
    # Complete this function
    length=len(s)
    multiple=len(s)//3
    p=0
    q=3
    count=0
    for i in range(multiple):
        new_sub_string=s[p:q]
        if new_sub_string[0]!='S':
            count+=1    
        if new_sub_string[1]!='O':
            count+=1
        if new_sub_string[2]!='S':
            count+=1   
        p=q
        q+=3
    return (count)
    

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)