n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if i*n in a:
        c+=1
print(c)
