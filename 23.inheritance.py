#inheritance
#1.Inheritance --> multiple , multi- level
#2.Data abstraction
#3.Encapsulation POJO
#4.Polymorphism
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("dog is barking")

dobj = Dog()
dobj.bark()
dobj.eat()
