class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


def length_of_list(head):

    count = 0
    current = head

    while current is not None:
        count += 1
        current = current.next

    return count

print(length_of_list(head))