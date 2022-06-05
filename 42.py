a=int(input())
b=int(input())
c=int(input())
d=(b*b)-(4*a*c)
ans=0
ans2=0
print(d)
if d>0:
    ans=(-b+(d)**0.5)/2*a
    ans2=(-b-(d)**0.5)/2*a
    print(int(ans))
    print(int(ans2))
elif d==0:
    ans=(-b+(d)**0.5)/2*a
    print(int(ans))
else:
    print(0)