a=int(input())
lst=[]
for i in range(a):
    x=int(input())
    lst.append(x)
print("TO interchange first and last element")
lst[0]=lst[-1]
