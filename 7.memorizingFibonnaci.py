#memorization fibonnaci sequence
#cache decorator ---> funtools
#0 1 1 2 3 5 8
#fn = (fn - 1) + (fn - 2)
def memorize(fibo):
    cache = {1:1,2:1}
    def inner(n):
        if n not in cache:
            cache[n] = fibo(n)
        return cache[n]
    return inner

@memorize
def fibo(n):
    print('Calculating fibo{0}'.format(n))
    return 1 if n<3 else fibo(n-1) + fibo(n-2)

print(fibo(6))
print('After printing fibo 6')
print(fibo(7))
print('After printing fibo 7')
print(fibo(10))
