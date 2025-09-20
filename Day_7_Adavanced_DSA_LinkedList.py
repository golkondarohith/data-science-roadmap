class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)

a.next = b
print(a.data, a.next.data)