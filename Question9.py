#x=int(input())
num=0
m=x
if x<0:
    return False
elif x==0:
    return True
else:
    while x>0:
        y=x%10
        num=num*10+y
        x=x//10
'''
    if num==m:
        state=True
    else:
        state=False  
print(state)
'''
return num==m
