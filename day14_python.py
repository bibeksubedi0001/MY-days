a=[]
i=1
while i<=10:
    b=i*i
    a.append(b)
    i+=1
print(a)
for value in a:
    print(value)


k=int(input("The_Searching_Number_is:"))
aa=(1,4,9,16,25,36,49,64,81,100)
i=1
for vlu in aa:
    if(vlu==k):
        print("found_HURRAY_in_Index_Number",i)
        break
    else:
        print('Hyaaa')
    i+=1