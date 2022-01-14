def flatten(l, new_list=[]):
    for i in l:
        if isinstance(i, list) or isinstance(i, dict):
            flatten(i, new_list)
        else:
            new_list.append(i)
    return new_list


daList = ['1', 4, [1, 2], [5, 6], [1, 'e'], {"c": 2}]
print(flatten(daList))


def flat_items(d, key_separator='.'):
    """
    Flattens the dictionary containing other dictionaries like here: https://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys

    >>> example = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}
    >>> flat = dict(flat_items(example, key_separator='_'))
    >>> assert flat['c_b_y'] == 10
    """
    for k, v in d.items():
        if type(v) is dict:
            for k1, v1 in flat_items(v, key_separator=key_separator):
                yield key_separator.join((k, k1)), v1
        else:
            yield k, v

