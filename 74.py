k=0
while k!=100:
    n=input()
    nl=n.split()
    ans=("red","blue","red","green")
    wr=str()
    for i in range(len(nl)):
        if nl[i] in ans:
            if nl[i]==ans[i]:
                wr+="1"
            else:
                wr+="2"
        else:
            wr+="3"
    if wr =="1111":
        print("正確答案")
        break
    else:
        print(wr)
    k+=1
    if k>=10:
        print("挑戰失敗")
        break