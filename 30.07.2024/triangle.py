a=int(input("Enter the number"))
for i in range(a):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(a):
    for j in range(a,i,-1):
        print("*",end=" ")
    print()
