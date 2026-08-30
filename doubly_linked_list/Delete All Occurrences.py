class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(10)
node4 = Node(30)
node5 = Node(10)


# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

node4.next = node5
node5.prev = node4


head = node1


# Delete all occurrences
def delete_all(head, value):

    current = head

    while current is not None:

        if current.data == value:

            # If current is head
            if current.prev is None:
                head = current.next

                if head is not None:
                    head.prev = None

            else:
                # Connect previous node to next node
                current.prev.next = current.next

                # Connect next node to previous node
                if current.next is not None:
                    current.next.prev = current.prev

        current = current.next

    return head


# Delete all 10s
head = delete_all(head, 10)


# Print list
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")