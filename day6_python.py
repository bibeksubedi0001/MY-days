marks=[94.4,98,97,98.7,99.4,"BIBEK"]
print(marks)
print(type(marks))
print(marks[5])
marks[5]=99.8
print(marks)
print(len(marks))
print(marks[0:3])
print(marks[0:len(marks)])
print(marks[:3])
marks.append(99.9)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(2,97.4)
print(marks)
marks.remove(94.4)
print(marks)
marks.pop(0)
print(marks)

#tuple
mark=(1,3,4,8,2,2,2,2,2,2,5)
a=(1)
print(type(a))
print(mark)
print(type(mark))
print(mark[0:2])
print(a)
print(mark.index(2))
print(mark.count(2))

a=input("Best movie:")
b=input("2nd Best movie")
c=input("3rd Best movie:")
print(d=[a,b,c])