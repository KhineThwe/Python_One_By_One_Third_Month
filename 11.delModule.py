import myModule
myModule.fibo(10)

del globals()['myModule']
myModule.fibo(10)
