# using for loop and if condition
def highest_num(l):
    max_num = l[0]
    for n in l:
        if max_num < n:
            max_num = n
    return max_num
print highest_num([3, 5, 6, 7, 8, 3])

# or using sorted
def highest_num(l):
    return sorted(l)[-1]

print highest_num([3, 5, 6, 7, 8, 3])


# or using sort

def highest_num(l):
    l.sort()
    return l[-1]

print highest_num([3, 5, 6, 7, 8, 3])

print sorted([3, 5, 6, 7, 8, 3])[-1]

