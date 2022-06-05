med=[]
meco=[]
num=int(input("輸入筆數N:"))
for i in range(num):
    n=str(input())
    s=int(input())
    med.extend(n)
    meco.append(s)
for k in range(len(meco)):
    print("%s牌得到 %d 面" % (med[k],meco[0]))