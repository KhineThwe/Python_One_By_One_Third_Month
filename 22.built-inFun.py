#class built in fun 4 ku shi tal
#1.getattr(obj's name,attr's name)
#2.setattr(obj,name,value) ဘယ် obj ထဲက ဘယ်attr ကို ဘယ်value set up
#3.delattr(obj,name)
#4.hasattr(obj,name) #return true ma shi yin false

class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
sobj = Student("NCCstu",101,24)
print(getattr(sobj,'name'))
setattr(sobj,'age',23)
print(getattr(sobj,'age'))
delattr(sobj,'age')
print(hasattr(sobj,'age'))
