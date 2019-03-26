X,Y=input().split()
X=list(X)
Y=list(Y)
c=0
if len(Y)>len(X):
    for i in range(len(Y)):
        if Y[i] not in X:
            c+=1
        else:
            if Y[i]!=X[i]:
                c+=1
else:
    for i in range(len(X)):
        if X[i] not in Y:
            c+=1
        else:
            if i<len(Y):
                if X[i]!=Y[i]:
                    c+=1
            else:
                c+=1

print(c)
