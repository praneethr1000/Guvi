x=int(input())
a=list(map(int,input().split()))
maxi=0
for i in range(x-1):
    cnt=1
    for j in range(i+1,x):
        if a[i]<a[j]:
            cnt+=1
        else:
            break
    if cnt>maxi:
        maxi=cnt
print(maxi)
