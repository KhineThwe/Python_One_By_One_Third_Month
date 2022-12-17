#method overloading arbitrary
#method 1 ku shi mal
class Price:
    def payment(self,*args):
        data = 0
        count = 0
        for i in args:
            count+=1
            data = data+i
        print("There are {0} parameters passed".format(count))
        return data
obj = Price()
print(obj.payment(6,7))
print(obj.payment(2,222,2,2,2,2,22,2))
