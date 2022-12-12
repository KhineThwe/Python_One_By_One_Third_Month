class myExcept(Exception):
    pass
class nameError(Exception):
    pass
class valueError(Exception):
    pass

try:
    a = 10
    b = 10
    if a is b:
        raise valueError
    else:
        raise nameError
except valueError:
    print("Value Error")
except nameError:
    print("Name Error")
