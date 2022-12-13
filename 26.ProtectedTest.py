#encapsulation
#private -----> __varname or __methodName
#protected ---> _varname or _methodName
class Base:
    def __init__(self,age):
        self._age = age #protected ဆိုသော်လည်း class ခေါ်သုံးလို့ရတယ်
        #modify လုပ်လို့ရ

class Sub(Base):
    def getData(self):
        print(self._age)

obj = Sub(100)
obj.getData()
# obj._age = 20
# print(obj._age)
# obj.getData()



