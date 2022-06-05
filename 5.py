n=int(input("請輸入階乘值M:"))
i=1
m=1
while m<n:
    i+=1    
    m*=i    
print("超過M為",n,"的最小階層N值為:",i)