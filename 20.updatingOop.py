#updating attr
#manually  ---> class ထဲမှာ method ရေးပြီး update လုပ်တာ class ရဲ့ outside မှ obj ကိုကိုင်ပြီးပြင်
#built - in
class Myclass:
    def __init__(self):
        self.name = "NCC"
        self.subject = "Python"
    def update(self):
        self.name = "ncc"
        self.subject = "c++"
o1 = Myclass()
o2 = Myclass()
print("Before Update")
print(o1.name,o1.subject)
print(o2.name,o2.subject)

# o1.update()
# o2.update()
o1.name = "kkk"
o1.subject = "django"
print("After Update")
print(o1.name,o1.subject)
print(o2.name,o2.subject)
