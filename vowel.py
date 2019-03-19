#praneeth
a1=input()
b=['A','E','I','O','U','a','e','i','o','u']
if a1 in b:
    print("Vowel")
elif a1.isalpha():
    print("Consonant")
else:
    print("invalid")
