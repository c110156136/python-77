acc=["123","456","789","336","775","566"]
psd=["456","789","888","558","666","221"]
money=[9000,5000,6000,10000,12000,7000]
ty=int(input("請輸入查詢組數:"))
for i in range(ty):
    t=input()
    s=t.split(" ")
    at=s[0]
    pt=s[1]
    for j in range(len(acc)):
        if at==acc[i]:
            if pt==psd[i]:
                print(money[i])                
        if at!=acc[i] or pt!=psd[i]:
            print("error")

        
                

               

