#opearator overloading
class People:
    def __init__(self,id,age):
        self.id = id#123
        self.age = age#40

    def __add__(self, other):
        data_id = self.id+other.id#123,124
        data_age = self.age+other.age#40,50
        return data_id,data_age

p1 = People(123,40)
p2 = People(124,50)
p3 = People(125,60)

total = p1+p2
# finalTotal = total+p3
did,dage = total
p4 = People(did,dage)
finalTotal = p4+p3
fid,fage = finalTotal
print("final result: ",fid,fage)

