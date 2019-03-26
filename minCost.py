X,Y=input().split()
X=list(X)
Y=list(Y)
c=0
for i in range(len(Y)):
    if Y[i] not in X:
        c+=1
    else:
        if Y[i]!=X[i]:
            c+=1
print(c)
