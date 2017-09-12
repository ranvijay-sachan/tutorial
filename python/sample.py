# class Ranvijay:
#     def __init__(self, name):
#         self.name = name
#         print "test"
#
#     def __call__(self, *args, **kwargs):
#         print self.name
#
# a = Ranvijay('ranvijay')
# print a()


# def calculate(arr):
#     for num in arr:
#         count = 0
#         for i in range(num +1):
#             if i % 2 != 0:
#                 count = count + i
#         print count
#
# calculate([3,1,2,3])


# def var_kwargs(farg, *args, **kwargs):
#     print "formal arg:", farg
#     for key in kwargs:
#         print "another keyword arg: %s: %s" % (key, kwargs[key])
#
# var_kwargs(farg=1, myarg2="two", myarg3=3)


