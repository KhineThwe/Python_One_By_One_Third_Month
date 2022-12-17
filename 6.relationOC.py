#relation
class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Child,Parent))
obj = Child()
print(isinstance(obj,Parent))
print(isinstance(obj,Child))
