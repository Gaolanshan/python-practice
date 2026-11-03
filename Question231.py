n=int(input())
state=False
if n<0:
    state=False
elif n==1:
    state=True
else:
    while n%2==0:
        n=n//2
        if n==1:
            state=True
            break
        elif n%2!=0:
            state=False
            break
return state