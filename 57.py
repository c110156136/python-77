n=input("請選擇主餐及升級的套餐:")
m=0
ln=list(n)
if ln[0]=="1":
    m=72
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
elif ln[0]=="2":
    m=62
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
elif ln[0]=="3":
    m=82
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
elif ln[0]=="4":
    m=44
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
elif ln[0]=="5":
    m=60
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
elif ln[0]=="1":
    m=72
    if ln[1]=="A":
        m+=55
    elif ln[1]=="B":
        m+=68
d=input("是否升級成大杯飲料:")
if d =="是":
    m+=7
f=input("是否換成大薯:")
if f =="是":
    m+=13
print("總共為",m,"元")