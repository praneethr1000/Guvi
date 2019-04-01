x=int(input())
t=0
for i in range(2,x//2+1):
    if x%i==0:
        print("no")
        t+=1
        break
if t==0:
    print("yes")
