# MRO(Method Resolution order) is the order in which python looks for a method in a hierarchy of classes.
# its play vital role in the context of multiple inheritance as single method may be found in multiple super classes.
# In computing, C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be
# inherited in the presence of multiple inheritance. In other words, the output of C3 superclass linearization is a
# deterministic Method Resolution Order (MRO).
# ALGO: C3 superclass linearization
# a consistent extended precedence graph,
# preservation of local precedence order, and
# fitting the monotonicity criterion.


class A:
    def do_this(self):
        print("I am in A")

class B(A):
    # def do_this(self):
    #     print("I am in B")
    pass

# class C(A, B): # this will not work TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
#     # def do_this(self):
#     #     print(" in C")
#     pass

# class D(B, B): # this will give error
#     # def do_this(self):
#     #     print("in D")
#     pass

class D(B, B): # this will give error
    def do_this(self):
        print("in D")

d1 = D()
d1.do_this()
