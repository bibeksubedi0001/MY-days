def show(n):
    print(n)
show(7)

def v(n):
    while(n>=1):
        print(n)
        n=n-1
v(7)

#Recursion
def v(n):
    if(n==0): #Base case
        return
    print(n)
    v(n-1)
v(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1)) 
print(fact(3))

def sum(n):
    if(n==1):
        return 1
    else:
        return(n+sum(n-1))
print(sum(10))

def list_print(list,index):
    if(index==len(list)):
        return
    print(list[index])
    list_print(list,index+1)
name=["BIBEK",99,100]
list_print(name,0)
