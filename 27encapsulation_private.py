#encapsulation private

class Parent:
    def __init__(self,age):
        self.__age = age

class Child(Parent):
    def modify(self,input):
        self.__age = input
        return self.__age
    def get_data(self):
        print(self.__age)

obj = Child(30)
print(obj.__dict__)
print(obj.modify(50))
print(obj.__dict__)
obj.get_data()



