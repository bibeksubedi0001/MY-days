class College:
    def __init__(self):
        print("ESTD")
    name="SSOS"
c=College()
print(c.name)

class College:
    def __init__(self,fullname):
        self.name=fullname
        print("ESTD")
c1=College("SSOS")
print(c1.name)
c2=College("GIS")
print(c2.name)

class College:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
c1=College("SSOS",73)
print(c1.name)
print(c1.marks)
c2=College("GIS",65)
print(c2.name)
print(c2.marks)