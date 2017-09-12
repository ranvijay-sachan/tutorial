# def linear_search(item, list):
#     found = False
#     position = 0
#     while position <= len(list) and not found:
#         if list[position] == item:
#             found = True
#         position = position + 1
#     return found


# def linear_search(obj, item, start=0):
#     for i in range(start, len(obj)):
#         if obj[i] == item:
#             return i
#     return -1


def linear_search(lst, item, start=0):
    for i in range(start, len(lst)):
        if lst[i] == item:
            return 1
    return -1

if __name__ == '__main__':
    print linear_search(['ranvijay', 'sachan', 'ranvijay2', 'ranvijay3'], 'ranvijay2')
