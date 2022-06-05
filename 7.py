price=input("請輸入月租費類型還有通話時間:")
ty=price.split(',')
sy=int(ty[0])
ti=int(ty[1])
if sy==186:
    ti*=0.09
    if ti>186:
        ti*=0.7
elif sy==386:
    ti*=0.08
    if ti>386:
        ti*=0.7
elif sy==586:
    ti*=0.07
    if ti>586:
        ti*=0.7
elif sy==986:
    ti*=0.06
    if ti>986:
        ti*=0.7
print(int(round(ti,0)))