n=int(input("Enter number of elements in list "))
l1=[]
for i in range(0,n):
    x=int(input("Enter the numbers in list "))
    l1.append(x)
print("Input: list1 = ",l1)
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print("Output: list2 = ",l2)