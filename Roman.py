#praneeth
n=list(input())
s=0
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in n:
    s=s+d[i]
print(s)
