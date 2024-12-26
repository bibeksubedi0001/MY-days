a=input("Best movie:")
b=input("2nd Best movie:")
c=input("3rd Best movie:")
d=[a,b,c]
print(d)
print(type(d))
g=[1,2,3,2] #palindrome

y=[1,3,5,1]
x=y.copy()
print(x)
y.reverse()
print(x)
print(y)
if x==y:
    print("palindrome")

s=("C","D","A","A","B","B","A")
t=s.count("A")
print(t)
v=["C","D","A","A","B","B","A"]
v.sort()
print(v)