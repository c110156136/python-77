n=[["123","456","789","321","654"],["Tom","Cat","NaNa","Lim","Won"],["DTGD","CSIE","ASIE","DBA","FDD"]]
s=input("請輸入學號:")
for i in range(3):
    if s==n[0][i]:
        print(s," ",n[1][i]," ",n[2][i])    