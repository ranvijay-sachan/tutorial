# find divisible number of 5 and not 7 between given range

lst = []

for i in range(4000, 4100):
    if (i % 5 == 0) and (i % 7 != 0):
        lst.append(i)

print lst
