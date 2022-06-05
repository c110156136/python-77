mapp=list()
ch=int(input("國文:"))
no=int(input("微積分:"))
en=int(input("英文:"))
pe=int(input("體育:"))
co=int(input("程式設計:"))
mapp.append(ch),mapp.append(no),mapp.append(en),mapp.append(pe),mapp.append(co)
av=(ch+no+en+pe+co)/5
ans=str()
ans2=str()
if max(mapp)==ch:
    ans="國文"
elif max(mapp)==no:
    ans="微積分"
elif max(mapp)==en:
    ans="英文"
elif max(mapp)==pe:
    ans="體育"
elif max(mapp)==co:
    ans="程式設計"
if min(mapp)==ch:
    ans2="國文"
elif min(mapp)==no:
    ans2="微積分"
elif min(mapp)==en:
    ans2="英文"
elif min(mapp)==pe:
    ans2="體育"
elif min(mapp)==co:
    ans2="程式設計"
print("平均分數:",'%.2f'%av)
print("最高分科目:",ans,max(mapp),"分")
print("最低分科目:",ans2,min(mapp),"分")