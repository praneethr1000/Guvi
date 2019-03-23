a=input()
b=list(a)
for i in range(0,len(b),2):
    t=b[i]
    b[i]=b[i+1]
    b[i+1]=t
print(''.join(b))
