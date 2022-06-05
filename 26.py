from itertools import count
d=str
while d!=0:
    d=input("檢測的字串(end結束):")
    if d=="end":        
        break
    n=input("檢測的單一字元:")
    c=d.count(n)
    print("字元",n,"出現次數為:",c)
print("檢測結束")