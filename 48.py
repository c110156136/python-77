n=int(input("輸入比數n:"))
dic=dict()
for i in range(n):
    s=input()
    q=s.split()
    dic[q[0]]=q[1]
o=input("輸入欲查詢單字:")
if o in dic:
    print(o,"的中文意思為",dic.get(o))
