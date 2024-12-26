list1=[4,5,6,7,8]
list=[99,1003,30077,100,110]
print(len(list),len(list1))


def length(list):
    print(len(list))
    print(*list)
    return length
rkk=[2,4,5,6,8,14,12]
ckk=[9,3,4,5,5,5]
length(rkk)
length(ckk)

def factorial(n):
    print()

a=int(input("Factorial of the number:"))
i=1
fact=1
while(i<=a):
    fact=i*fact
    i+=1
print("is:",fact)

def fac(n):
    i=1
    fact=1
    while(i<=n):
        fact=i*fact
        i+=1
    print("is:",fact)
    return fac
fac(6)
fac(9)

def value(a):
    b=a*585.65
    print("The value in INR is:",b)
    return value
x=float(input("Enter the USD: "))
value(x)

def nature(z):
    if(z%2==0):
        print("EVEN")
    else:
        print("ODD")
        return nature
k=int(input("The_Number_is: "))
nature(k)
