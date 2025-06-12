 
#practice_question_1  
i=1
while i<=100:
    print(i)
    i+=1

#practice_question_2
j=100
while j>0:
    print(j)
    j-=1
#practice_question_3

a=int(input("A number"))
n=1
while n<=10:
    aa=a*n
    print(aa)
    n=n+1

#practice_question_4   
b=1
g=[]
while b<=10:
    k=b*b
    g.append(k)
    b+=1
print(g)
ss=0
while ss<=9:
    print(g[ss])
    ss+=1


#practice_question_5
t=1
r=int(input("Searchin Number is:"))
h=[]
while t<=10:
    q=t*t
    if q==r: 
        print("Found","Index_Number is:",t)
    h.append(q)
    t+=1
print(h)

#practice_question_6
u=int(input("Searching_Number is:"))
ap=(1,4,9,16,25,36,49,64,81,100,121,144)
ii=0
while ii<=11:
    if(u==ap[ii]):
        print("Found_the_multiple_of_:",ii+1)
    ii+=1
    



