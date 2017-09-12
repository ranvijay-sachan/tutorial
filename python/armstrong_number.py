"""
An Armstrong number of three digits is an integer such that the sum of the cubes of 
its digits is equal to the number itself. For example, 371 is an Armstrong number 
since 3**3 + 7**3 + 1**3 = 371. Write a program 
to find all Armstrong number in the range of 0 and 999.
"""

number = 371
temp = int(number)
sum = 0

while temp !=0:
    rem = temp %10
    sum +=(rem * rem * rem)
    temp = temp / 10

if sum ==number:
    print True
else:
    print False
