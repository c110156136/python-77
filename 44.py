n=int(input())
if n>10:
    print("1~10")
    n=int(input())
li=list()
for i in range(n):
    s=input()
    li.append(s)
print(max(li),"台")