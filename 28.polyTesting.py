#polymorphism
class AgAg:
    def human(self):
        print("Ag Ag is a programmer")
        print("Ag Ag is always coding")

class MgMg:
    def human(self):
        print("Mg Mg is a hacker")
        print("Mg Mg is always learning")

class KoKo:
    def human(self):
        print("Ko Ko is an actor")
        print("Ko Ko is always fighting")

class People:
    def fun(self,obj):
        obj.human()
agag = AgAg()
mgmg = MgMg()
koko = KoKo()
people = People()
people.fun(mgmg)

myList = [agag,mgmg,koko]
for obj in myList:
    people.fun(obj)
