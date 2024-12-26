def cal(a,b):
    sum=a+b
    print(sum)
    return sum
cal("a","b")
cal(1,2)

def mul(a,b):
    k=a*b
    print(k)
    return k
mul(4,5)
mul(8,1)
mul(4.5,4.5)

def s(a,b,c):
    s=(a+b+c)/3
    print(s)
    return s
i=1
g=[]
while i<=3:
    a=int(input("Enter the number:"))
    g.append(a)
    i+=1
s(*g) # Call the function with the user input
s(4,3,5)
s(5,2,9)
