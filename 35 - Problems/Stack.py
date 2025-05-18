class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        
my_book_stack = stack()
my_book_stack.push("Atomic Habits")
my_book_stack.push("Alchemist")
my_book_stack.push("The stle art of not giving fu*k")
print(my_book_stack)
