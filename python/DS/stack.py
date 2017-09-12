class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
print s.items

# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.is_empty():
#                 balanced = False
#             else:
#                 s.pop()
#
#         index = index + 1
#
#     if balanced and s.is_empty():
#         return True
#     else:
#         return False
#
#
# print(parChecker('((()))'))
# print(parChecker('(()'))