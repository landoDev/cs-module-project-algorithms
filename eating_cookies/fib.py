def fib(n, cache={}):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # Base cases
        return n
    # check if there is a cache
    elif n in cache:
        print("grabbing from cache[%i]" % n)
        return cache[n]

    print("computing fib(%i)" % n)
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
            
    return cache[n]


print(fib(40))