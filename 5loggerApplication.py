#logger
def logger(fn):
    from functools import wraps
    from datetime import datetime,timezone
    @wraps(fn)
    def inner(*args,**kwargs):
        dt = datetime.now(timezone.utc)
        result =fn(*args,**kwargs)
        print('{0} : called {1}: recent data: {2}'.format(dt,fn.__name__,result))
        return result
    return inner

@logger
def myFun(x,y):
    """From fun 1"""
    return x+y

myFun(10,20)
print(myFun.__doc__)
