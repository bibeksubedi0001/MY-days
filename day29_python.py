#Class & Instance Attributes
class Student:
    abc="EEMA"
    name="to_be_defined"
    def __init__(self,name,symbol_number):
        self.name=name  #obj attr > class attr
        self.symbol=symbol_number
name1=Student("shyam",1048393)
name2=Student("golden",948393)
print(name1.name,name1.symbol,Student.abc)
print(name2.name,name2.symbol,Student.abc)
