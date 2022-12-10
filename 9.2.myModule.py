def fibo(n):
    """normal fibo"""
    a,b=0,1
    while a<n:
        print(a , end=' ')
        a,b = b,a+b

def listFibo(n):
    """List fibo"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
