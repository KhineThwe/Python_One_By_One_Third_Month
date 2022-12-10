#memorization fibonnaci sequence
#cache decorator ---> funtools
#0 1 1 2 3 5 8
#fn = (fn - 1) + (fn - 2)
def memorize(fibo):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fibo(n)
        return cache[n]
    return inner

@memorize
def fact(n):
    print('Calculating factorial{0}'.format(n))
    return 1 if n<2 else n*fact(n-1)

print(fact(6))
#6*5*4*3*2*1 -----> 720
print(fact(7))
print(fact(10))

