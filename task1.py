def caching_fibonacci(n, cache={}):
    if n < 0:                           
        raise ValueError

    def fibonacci(n):                      
        if n <= 0: return 0                
        if n == 1: return 1                
        if n in cache: return cache[n]   
     
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(n)

print(caching_fibonacci(10))
print(caching_fibonacci(15))