first_list = [1, 2]
second_list = [3, 1]
third_list = [100, 0, 1]

# using set
resulting_list = first_list + list(set(second_list) - set(first_list))
resulting_list.sort()
print resulting_list

# using list comprehension

resulting_list = first_list + [i for i in second_list if i not in first_list]
resulting_list.sort()
print resulting_list

resultList = list(set(first_list) | set(second_list) | set(third_list))
resultList.sort()
print resultList


