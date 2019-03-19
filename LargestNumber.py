#praneeth
n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[::-1]
x=0
for i in b:
    x=x*10+i
print(x)
