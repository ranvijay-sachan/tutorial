def some_func(var, *args, **kwargs):
    print var
    for x in args:
        print('{}').format(x)

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


if __name__ == '__main__':
    some_func('ranvijay', [1,2,3], [1,2,3], name=[1,2,3,4,5], rol=[1,2,3,4,5])