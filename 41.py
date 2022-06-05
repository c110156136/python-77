n=int(input("搭了幾次電梯:"))
if n> 10:
    print("1~10")
    n=int(input("搭了幾次電梯:"))
m=0
f=list()
for i in range(n):
    s=input()
    f.append(s)
    if i==0:
        m+=(int(s)-1)*20
    if f[i]>f[i-1]:
        m+=(int(f[i])-int(f[i-1]))*20
    elif f[i]<f[i-1]:
        m+=(int(f[i-1])-int(f[i]))*10
print(m,"元")