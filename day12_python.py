a=7
while a<=15:
    print(a)
    if(a==9):
        break
    a+=1

k=[]
m=int(input("The_Searching_Number:"))
b=1
while(b<100):
    print(b)
    k.append(b)
    if(b==m):
        break
    b+=1
print("Found",b)
print(k)

i=0
while i<=5:
    if(i==3):
        i+=1
        continue    #skip
    print(i)
    i+=1

m=0
while m<=20:
    if(m%2!=0):
        m+=1
        continue
    print(m)
    m+=1



