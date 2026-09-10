class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def removeDuplicates(head):

    current = head

    while current is not None and current.next is not None:

        # Check if current and next node are duplicates
        if current.data == current.next.data:

            # Skip the duplicate node
            current.next = current.next.next

            # Fix backward connection
            if current.next is not None:
                current.next.prev = current

        else:

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
node3 = Node(20)
node4 = Node(30)
node5 = Node(30)
node6 = Node(30)
node7 = Node(40)

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
node6.next = node7

node7.prev = node6


head = node1

print("Original:")
printList(head)

head = removeDuplicates(head)

print("After Removing Duplicates:")
printList(head)