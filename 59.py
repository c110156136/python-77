s=list()
for i in range(10):
    n=input("請輸入第{}個數字:".format(i+1))
    s.append(int(n))
ss=sorted((s))
print("最大的三個數字為:",ss[9],",",ss[8],",",ss[7])
print("最小的三個數字為:",ss[0],",",ss[1],",",ss[2])