#method overloading
#method 1 ku shi mal
class Price:
    def payment(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return None
obj = Price()
print(obj.payment(6,7))
