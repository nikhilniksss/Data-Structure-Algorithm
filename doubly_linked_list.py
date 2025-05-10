# implementation of doubly linked list

class ListNode:
    def __init__(self,val):
        self.value = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index:int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head

        while index != 0:
            cur = cur.next
            index -= 1

        return cur.val
    
    def addAtHead(self,val : int)-> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self,val:int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


