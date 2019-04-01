x=list(input())
y=x[::-1]
t=0
for k in range(len(x)):
    if x[k]!=y[k]:
        t+=1
        print("no")
        break
if t==0:
    print("yes")
