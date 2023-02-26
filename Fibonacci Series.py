x=int(input("Enter how many numbers you want to print from the Fibonacci series "))
a=0
b=1
print(a)
print(b)
for i in range (x-2):
    sum=a+b
    a=b
    b=sum
    print(sum)
