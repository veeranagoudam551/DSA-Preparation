class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(20)
node4 = Node(30)
node5 = Node(30)
node6 = Node(40)


# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

node4.next = node5
node5.prev = node4

node5.next = node6
node6.prev = node5


# Head
head = node1


# Remove duplicates
def remove_duplicates(head):

    current = head

    while current is not None and current.next is not None:

        if current.data == current.next.data:

            # Skip the duplicate node
            current.next = current.next.next

            # Fix the backward connection
            if current.next is not None:
                current.next.prev = current

        else:
            current = current.next

    return head


# Remove duplicates
head = remove_duplicates(head)


# Print the list
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")