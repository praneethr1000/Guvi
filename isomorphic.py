a,b=input().split()
c=len(set(list(a)))
b=len(set(list(b)))
if c==b:
    print("yes")
else:
    print("no")
