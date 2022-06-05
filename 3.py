year=int(input("請輸入西元年份:"))
ani=str()
n=(year%12)-4
if n==0:
    ani="rat"
elif n==1:
    ani="ox"
elif n==2:
    ani="tiger"
elif n==3:
    ani="rabbit"
elif n==4:
    ani="dragon"
elif n==5:
    ani="snake"
elif n==6:
    ani="horse"
elif n==7:
    ani="goat"
elif n==8:
    ani="monkey"
elif n==9:
    ani="rooster"
elif n==10:
    ani="dog"
elif n==11:
    ani="pig"
print(ani)