# def line_check_out():
#     word="in"
#     data=True
#     line=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line)
#             line+=1
#     return -1
# line_check_out()

with open("numbers.txt","r") as f:
    data=f.read()
    print(data)
    numbers=data.split(",")
    print(numbers)
    i=0
    a=0
    while(i<len(numbers)):
        if(int(numbers[i])%2==0):
            a+=1
            print("NUM is the EVEN") 
        else:
            print("NUM is the ODD")
        i+=1
    print("The Number of Even Numbers are:",a)