f=open("practice.txt","w")
f.write("Hi everyone\nwe are learing File I/O\nusing Java.\nI like programming in Java.")

f=open("practice.txt","r+")
text_data=f.read()
new_text_data=text_data.replace("Java","Python")
print(new_text_data)
f=open("practice.txt","w")
f.write(new_text_data)

word="learning"
f=open("practice.txt","r")
data=f.read()
if (data.find(word)!=-1):
    print("FOUND")
else:
    print("NOT!")

