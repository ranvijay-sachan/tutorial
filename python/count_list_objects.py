def custom_count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total = total + 1
    return total


lst = [1, 2, 1, 2, 2, 5, 5, 5, 5, '5', 1, 2, 1, 2, 2, 5, 5, 5, 5, '5']
print {i: custom_count(lst, i) for i in lst}
