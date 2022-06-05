n=int(input("組數為:"))
for i in range(1,n+1):
    do=input("請輸入全票半票:")
    s=do.split()
    p=int(s[0])*250+int(s[1])*175
    print("第",i,"組的總價為:",p)