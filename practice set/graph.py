# implementation of graph algorithm

class Node():
    def __init__(self,value):
        self.value = value
        self.adjecent_list = []
        self.visited = False

class Graph():
    pass

node1 = Node("A") 
node2 = Node("B") 
node3 = Node("C") 
node4 = Node("D") 
node5 = Node("E") 
node6 = Node("F") 
node7 = Node("G")

node1.adjecent_list.append(node2)
node1.adjecent_list.append(node3)
node1.adjecent_list.append(node4)

node2.adjecent_list.append(node5)
node2.adjecent_list.append(node6)
node4.adjecent_list.append(node7)