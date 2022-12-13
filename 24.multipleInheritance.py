#multiple inheritance
class Parent:
    def parent(self):
        print("This is from parent")

class Aunty:
    def aunty(self):
        print("This is from aunty")

class Uncle:
    def uncle(self):
        print("This is from uncle")

class Child(Parent,Aunty,Uncle):
    def child(self):
        print("This is from chile")

cobj = Child()
cobj.aunty()
