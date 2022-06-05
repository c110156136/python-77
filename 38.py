n=int(input())
if n>10 or n<2:
    print("重新輸入(2~10之內)")
    n=int(input())
u=list()
while n!=0:
    s=int(input())
    if s>1000 or s<1:
        print("重新輸入")
        s=input()
    u.append(s)
    n-=1
for i in range(len(u)):
    if u[i]%9==0 or u[i]%11==0:
        print("第",i+1,"個點",u[i])
