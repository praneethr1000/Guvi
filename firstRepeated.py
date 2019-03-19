n=int(input())
a=list(map(int,input().split()))
b=[]
t=0
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)
        t+=1
        break
if t==0:
    print("unique")
