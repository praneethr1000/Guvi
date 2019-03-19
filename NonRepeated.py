b=int(input())
a=list(map(int,input().split()))
a.sort()
t=0
for i in range(0,b - 1,2):
    if a[i] != a[i + 1]:
        print(a[i])
        t += 1
        break
if t == 0:
    print(a[-1])

