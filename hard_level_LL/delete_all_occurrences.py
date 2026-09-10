class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def delete_all_occurrences(head, key):

    current = head

    while current is not None:

        # If current node contains the key
        if current.data == key:

            # If current is the head
            if current == head:

                head = current.next

                # If list still has nodes
                if head is not None:
                    head.prev = None

            else:

                # Connect previous node to next node
                current.prev.next = current.next

                # Connect next node to previous node
                if current.next is not None:
                    current.next.prev = current.prev

        # Move to next node
        current = current.next

    return head


def printList(head):

    current = head

    while current is not None:

        print(current.data, end=" ⇄ ")
        current = current.next

    print("None")


# -------------------------
# Create DLL
# -------------------------

node1 = Node(10)
node2 = Node(20)
node3 = Node(10)
node4 = Node(30)
node5 = Node(10)
node6 = Node(40)

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


head = node1

print("Original:")
printList(head)


# Delete all 10s
head = delete_all_occurrences(head, 10)


print("After deleting 10:")
printList(head)