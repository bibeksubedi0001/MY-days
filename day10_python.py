#sets in python
a={1,2,"name","4","5"}
print(a)
b=[2,4,83]
print(b)
print(a.union(b))
print(type(a),type(b))
print(b[2])
e={} #empty dict not empty sett
d=set() #empty set
print(type(d))
a.add(5)
a.add(34)
a.add("dg")
print(a)
a.remove(34)
print(a)
x=a.pop()
print(x)
print(a)
m={3,4,2,4,2,4,1,5,6,7}
j={3,53,6,46,2,6,364}
print(m.union(j))
print(j.intersection(m))



