#OOP
#PEP 8
#attribute ---> var ---> in other property
#behavior --->
#method
class Myclass:
    def __init__(self,xAxis,yAxis):
        self.xAxis = xAxis#obj1.xAxis = 10
        self.yAxis = yAxis#obj1.yAxis = 20

    def normal_method(self):
        print("This is normal method")

obj1 = Myclass(10,20)#constructor obj
print(obj1.xAxis,obj1.yAxis)
obj1.normal_method()
# obj1.myFun()
# obj2 = Myclass()
# if id(obj1) == id(obj2):
#     print("Addresss are equal")
# else:
#     print("They are not same")
