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



# Stack using link list


'''Python supports automatic garbage collection so deallocation of memory
is done implicitly. However to force it to deallocate each node after use,
add the following code:
 
    import gc         #added at the start of program
    gc.collect()     #to be added wherever memory is to be deallocated
'''
 
class Node:
     
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
     
    # head is default NULL
    def __init__(self):
        self.head = None
     
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
     
    # Remove element that is the current head (start of the stack)
    def pop(self):
         
        if self.isempty():
            return None
             
        else:
            # Removes the head node and makes
            #the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
     
    # Returns the head node data
    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
     
    # Prints out the stack    
    def display(self):
         
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return
         
# Driver code
MyStack = Stack()
 
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)
 
# Display stack elements
MyStack.display()
 
# Print top element of stack
print("\nTop element is ",MyStack.peek())
 
# Delete top elements of stack
MyStack.pop()
MyStack.pop()
 
# Display stack elements
MyStack.display()
 
# Print top element of stack
print("\nTop element is ", MyStack.peek())
