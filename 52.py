st1="紅豆生南國，春來發幾枝?願君多采擷，此物最相思。"
st2="春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少?"
li1=list(st1)
li2=list(st2)
ans=list()
for i in range(len(st1)):
        if li1[i]in li2:
            ans.append(li1[i])
        if li1[i]=="，":
            ans.remove(li1[i])
        if li1[i]=="。":
            ans.remove(li1[i])
        if li1[i]=="?":
            ans.remove(li1[i])
print(ans)