'''
     *
    **
   ***
  ****
 *****
'''

for g in range(6, 0, -1):
    print(g * ' ' + (6 - g) * '*')

print '\n'

'''
* * *
* *
*
'''

for i in range(1, 4):
    for j in range(3, i - 1, -1):
        print "*",
    print

print '\n'

'''
1 
2 2 
3 3 3 
4 4 4 4
'''

for i in range(5):
    print (str(i) + " ") * i

print '\n'

''''
1 
2 1 
3 2 1 
4 3 2 1
'''
for i in range(1, 4 + 1):
    for j in range(i, 0, -1):
        print(j),
    print("")
