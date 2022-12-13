#multi-level inheritance
class Parent:
    def parent(self):
        print("This is from parent")

class Aunty(Parent):
    def aunty(self):
        print("This is from aunty")

class Uncle(Aunty):
    def uncle(self):
        print("This is from uncle")

class Child(Uncle):
    def child(self):
        print("This is from chile")

cobj = Child()
cobj.parent()
