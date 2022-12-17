#method overloading arbitrary string
class Price:
    def payment(self,dataType,*args):
        if dataType == "int":
            data = 0
            count = 0
            for i in args:
                count += 1
                data = data + i
            print("There are {0} parameters passed".format(count))
            return data
        elif dataType == "str":
            data = ''
            count = 0
            for i in args:
                count+=1
                data = data+i
            print("There are {0} parameters passed".format(count))
            return data
obj = Price()
print(obj.payment('int',6,7))
print(obj.payment('int',2,222,2,2,2,2,22,2))
print(obj.payment('str','aung','2'))
