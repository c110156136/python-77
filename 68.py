n1=input("請輸入第一個數字:")
if len(n1)>6 or len(n1)<2:
    print("長度2~6")
    n1=input("請輸入第一個數字:")
n2=input("請輸入第二個數字:")
if len(n2)>6 or len(n2)<2:
    print("長度2~6")
    n2=input("請輸入第二個數字:")
elif len(n1)!=len(n2):
    print("長度不同")
    n2=input("請輸入第二個數字:")
n1l=list(n1)
n2l=list(n2)
A=0
B=0
for i in range(len(n1l)-1):
    if n1l[i] in n2l:
        if n1l[i]==n2l[i]:
            A+=1
        else:
            B+=1
if A==4:
    print(A,"A",B,"B 全對")
else:
    print(A,"A",B,"B 加油")