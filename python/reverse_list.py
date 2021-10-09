# using slices
a = [1, 2, 3, 4]

print a[::-1]

# or using reverse method

a.reverse()
print a

#using manaul

x = [3, 4, 100, 34, 45]
for i in range(len(x) - 1):
    if x[i] > x[i + 1]:
        x[i],x[i + 1] = x[i + 1], x[i]
print (x)
