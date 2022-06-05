import math
n=float(input("請輸入路程公里數(km):"))
m=0
if n<=1.5:
    m=75
elif n > 1.5:    
    x=(n-1.5)/0.25
    m=75 + math.ceil(x)*5
print("所需車資為:",m,"元")
