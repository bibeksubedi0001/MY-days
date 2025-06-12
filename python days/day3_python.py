a="red"
b="green"
c="blue"
d="whitish"
e=input("visible light")
if(e==a):
    print("stop")
elif(e==b):
    print("goooo")
elif(e==d):
    print("looook")
else:
    print("bro_ken")

marks=int(input("MARKS"))
if(marks<59):
    print("Not good")
elif(marks==59):
    print("Satisfactory")
else:
    print("Perfect")    

a=input("Grades:")
passs="yes" if a=="Good" else"No"
print(passs)

k=float(input("Percentage is "))
Good="Nice" if k>73.56 or k<23 else "Xee"
print(Good)

age=int(input("age:"))
vote= ("yes","no") [age>=18]
print(vote)

a=int(input("First Number is:"))
b=int(input("Second is:"))
print("True") if(a>=b) else print("False")