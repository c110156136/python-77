dri=["10","20","30","40","50"]
mo=input("身上有多少錢:")
co=0
for i in range(len(dri)):
    if mo>=dri[i]:
        co+=1
print(co,"種")