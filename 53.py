n=int(input("輸入n值:"))
ch=dict()
for i in range(n):
    s=input("請輸入姓名:")
    q=input("請輸入電子郵件:")
    ch[s]=q
che=input("請輸入要查詢電子郵件的姓名:")
if che in ch:
    print(che,"的電子郵件帳號為:",ch.get(che))
