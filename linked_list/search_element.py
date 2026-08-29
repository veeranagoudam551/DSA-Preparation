class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head
head = node1


# Search in Linked List
def search_list(head, target):

    current = head

    while current is not None:

        if current.data == target:
            return True

        current = current.next

    return False


# Take target from user
target = int(input("Enter the value to search: "))

print(search_list(head, target))