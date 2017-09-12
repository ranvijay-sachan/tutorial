def flatten(l, new_list=[]):
    for i in l:
        if isinstance(i, list) or isinstance(i, dict):
            flatten(i, new_list)
        else:
            new_list.append(i)
    return new_list


daList = ['1', 4, [1, 2], [5, 6], [1, 'e'], {"c": 2}]
print(flatten(daList))


