class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

head = node1


# Delete head
def delete_head(head):

    if head is None:
        return None

    head = head.next

    if head is not None:
        head.prev = None

    return head


head = delete_head(head)


# Print list
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")