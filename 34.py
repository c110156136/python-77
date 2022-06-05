n=int(input("輸入一正整數:"))
ans=str()
if n>100 or n<11:
    print("請輸入正確的值")
    n=int(input("輸入一正整數:"))
else:
    if n%11==0 and n%2==0:
        ans="Yes"
    else:
        ans="No"
print(n,"為新公倍數?:",ans)