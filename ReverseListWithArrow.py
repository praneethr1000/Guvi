n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
for i in range(n):
    if i!=n-1:
        print(b[i],end='->')
    else:
        print(b[i])
