#property @
def myDec1(fn):
    def inner():
        print('Running decorator 1')
        return fn()
    return inner

def myDec2(fn):
    def inner():
        print('Running decorator 2')
        return fn()
    return inner

@myDec1
@myDec2
def myFun():
    print("Running my fun")

# result = myDec1(myDec2(myFun))
# result()
myFun()
