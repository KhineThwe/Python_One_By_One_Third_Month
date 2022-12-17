#method overriding
class Price():
    def payment(self):
        print("From Parent class")
class Child(Price):
    def payment(self):
        print("From Child Class")
class GrandChild(Child):
    def payment(self):
        print("From GrandChild Class")
obj = GrandChild()
obj1 = Child()
obj1.payment()
obj.payment()
