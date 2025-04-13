n=int(input("Enter a number "))
a=n
f=1
i=1
for i in range (1,a):
    f=f*i
    n=n-1
    i=i+1
    print(f"The factorial of {a} is {f}")
