n=input("請輸入一串小寫英文:")
ln=list(n)
u=str()
for i in range(len(ln)):
    if "a" ==ln[i] :
        ln[i]="."
    if "e" ==ln[i] :
        ln[i]="."
    if "i" ==ln[i] :
        ln[i]="."
    if "o" ==ln[i] :
        ln[i]="."
    if "u" ==ln[i] :
        ln[i]="."
    u+=ln[i]
print(u)