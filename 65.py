n=input("請輸入A的好友:")
nl=n.split()
nb=input("請輸入B的好友:")
nbl=nb.split()
ans=list(set(nl).intersection(set(nbl)))#取交集
print(len(ans))