n=input("請輸入五張牌:")
s=n.split(' ')
c=0
for i in range(4):
    if s[i]=="A":
        c+=1
    elif s[i]=="J" or s[i]=="j":
        c+=11
    elif s[i]=="Q":
        c+=12
    elif s[i]=="K":
        c+=13
    else:
        c+=int(s[i])
print(c)
