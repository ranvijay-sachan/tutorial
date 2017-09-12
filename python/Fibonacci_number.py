'''

a series of numbers in which each number ( Fibonacci number ) 
is the sum of the two preceding numbers. 
The simplest is the series 1, 1, 2, 3, 5, 8, etc.

'''

num = int(input("enter number"))


def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    for i in range(num):
        print fib(i)
