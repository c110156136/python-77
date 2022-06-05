n=int(input())
while n!=0:
    u=str()
    q=list()
    p=0
    d=0
    for i in range(4):
        s=int(input())
        u+=str(s)
        u+=" "
        q.append(s)
    if q[3]-q[2]==q[2]-q[1]==q[1]-q[0]:        
        u+=str(q[3]+(q[3]-q[2]))
        print(u)
        print("此為等差數列")
    elif q[3]//q[2]==q[2]//q[1]==q[1]//q[0]:
        u+=str(q[3]*(q[3]//q[2]))
        print(u)
        print("此為等比數列")
    n-=1