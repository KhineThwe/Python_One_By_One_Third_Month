#wrap ----> funtools
#function တစ်ခုသည် decorator ထဲကိုဖြတ်ပြီဆိုတာနဲ့ doc string တွေသည် လုံးဝပျောက်သွားတယ်
#to solve that problem ---> use @wrap
from functools import wraps
def log(fn):
    @wraps(fn)
    def with_log(*args,**kwargs):
        print(fn.__name__+"was called")
        return fn(*args,**kwargs)
    return with_log

@log
def myFun(x):
    """Some operation just like arithmetic"""
    return x+x+x

@log
def myFun2(x):
    """From myFun2"""
    return x+x+x

myFun(5)
print(myFun.__name__)
print(myFun.__doc__)

myFun2(20)
print(myFun2.__name__)
print(myFun2.__doc__)



