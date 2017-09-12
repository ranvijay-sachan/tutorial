'''
n! = n*(n-1)!

n	n!
1	1	                     1
2 * 2              = 2*1!   =2 
3* 2 * 2 * 1       = 3*2!   =6
4 * 3* 2 * 2 * 1   = 4*3!   =24
'''

fact =1
for i in range(4):
    fact = fact*(i+1)

print fact
