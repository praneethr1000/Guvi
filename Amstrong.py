N=int(input())
s=0
t=N
while(N>0):
    x=N%10
    s=s+(x*x*x)
    N=N//10
if s==t:
    print("yes")
else:
    print("no")
