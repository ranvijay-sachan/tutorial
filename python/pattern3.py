from __future__ import print_function

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
for i in range(0, 5):
    for j in range(0, i + 1):
        print("* ", end="")
    print()


'''
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * *
'''
k = 1
for i in range(0, 5):
    for j in range(0, k):
        print("* ", end="")
    k = k + 2
    print()
