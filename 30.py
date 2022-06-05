q=1
while q==1:
    n=input("請輸入四個數字:")
    if n=="0000":
        break
    s=list(n)
    ans="1234"
    a=0
    b=0
    ansty=list(ans)
    for i in range(4):
        if s[i] in ans:
            if s[i]==ansty[i]:
                a+=1
            else:
                b+=1
    print(a,"A",b,"B")
    if a==4:
        print("猜對了!!!")
        break