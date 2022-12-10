#timer application
def logger(fn):
    from functools import wraps
    from datetime import datetime,timezone

    @wraps(fn)
    def inner(*args,**kwargs):
        dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print('{0} : called {1}: recent data : {2}'.format(dt,fn.__name__,result))
        return result
    return inner

def timer(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args,**kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        realTime = end - start
        print('function {0} run for {1:.6f}'.format(fn.__name__,realTime))
        return result
    return inner

@logger
@timer
def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

print(fact(10))
