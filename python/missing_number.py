def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


lst = [3, 4, 7, 1, 9, 1]
print(find_missing(sorted(lst)))
