n1=int(input())
n2=int(input())
s=(n1*2|n2)%3
if s ==0:
    print("普通")
elif s ==1 :
    print("吉")
else:
    print("大吉")