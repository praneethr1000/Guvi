n=input()
b=n.split()
x=len(b)
for i in range(x):
    t=b[i]
    if i!=x-1:
        print(t[::-1],end=' ')
    else:
        print(t[::-1])
