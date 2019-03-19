n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=a[::-1]
for i in range(k):
    if i==k-1:
        print(b[i])
