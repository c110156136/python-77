m=input("請輸入月份以及日期:")
d=m.split(' ')
month=int(d[0])
day=int(d[1])
if month==1:
    if day<21:
        print("Capricorn")
    else:
        print("Aquarius")
if month==2:
    if day<19:
        print("Aquarius")
    else:
        print("Pisces")
if month==3:
    if day<22:
        print("Pisces")
    else:
        print("Aries")
if month==4:
    if day<21:
        print("Aries")
    else:
        print("Taurus")
if month==5:
    if day<22:
        print("Taurus")
    else:
        print("Gemini")
if month==6:
    if day<22:
        print("Gemini")
    else:
        print("Cancer")
if month==7:
    if day<23:
        print("Cancer")
    else:
        print("Leo")
if month==8:
    if day<23:
        print("Leo")
    else:
        print("Virgo")
if month==9:
    if day<23:
        print("Virgo")
    else:
        print("Libra")
if month==10:
    if day<24:
        print("Libra")
    else:
        print("Scorpio")
if month==11:
    if day<23:
        print("Scorpio")
    else:
        print("Sagittarius")
if month==12:
    if day<22:
        print("Sagittarius")
    else:
        print("Capricorn")