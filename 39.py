from tkinter import N


n=int(input())
s=n//2+1
for i in range(s):
    print((s-i)*" "+(2*i+1)*"*")
for q in range(s):
    print(" "*(q+2)+"*"*((n-2)-(2*q)))