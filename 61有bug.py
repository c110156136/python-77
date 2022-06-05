n=input("請輸入遊戲時間:")
s=n.split(":")
mi=int(s[0])*60
to=mi+int(s[1])-75
ti=int(to/30)
mo=0
for i in range(1,ti+1):
    if i%3==0:
        mo+=7
    else:
        mo+=6
mo-=int(ti/2)
print(mo,"隻兵")
