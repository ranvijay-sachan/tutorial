from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print 'Elapsed time: {}'.format(end - start)
        return result

    return wrapper


@timing
def f(a):
    for _ in range(a):
        print "Ranvijay"


print(f(2))


# Decorator with parameter

def salute(msg):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            return msg + args[0]
        return wrapper
    return decorator
    
    
@salute("HI, ")
def greet(name):
    print(name)
    
    
print(greet("Amit")) #HI, Amit
