class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Function to add two linked lists
def addTwoNumbers(l1, l2):

    # Dummy node for result
    dummy = Node(0)
    current = dummy

    # Initially no carry
    carry = 0

    # Continue until both lists and carry are finished
    while l1 is not None or l2 is not None or carry:

        # Get value from l1
        if l1 is not None:
            val1 = l1.data
        else:
            val1 = 0

        # Get value from l2
        if l2 is not None:
            val2 = l2.data
        else:
            val2 = 0

        # Add values and carry
        total = val1 + val2 + carry

        # Get digit
        digit = total % 10

        # Get carry
        carry = total // 10

        # Create new node
        current.next = Node(digit)

        # Move current forward
        current = current.next

        # Move l1 forward
        if l1 is not None:
            l1 = l1.next

        # Move l2 forward
        if l2 is not None:
            l2 = l2.next

    # Return actual result (skip dummy)
    return dummy.next


# Function to print linked list
def printList(head):

    current = head

    while current is not None:

        print(current.data, end=" → ")

        current = current.next

    print("None")


# -------------------------
# CREATE FIRST LINKED LIST
# -------------------------

# l1 = 2 → 4 → 3

node1 = Node(2)
node2 = Node(4)
node3 = Node(3)

node1.next = node2
node2.next = node3

l1 = node1


# -------------------------
# CREATE SECOND LINKED LIST
# -------------------------

# l2 = 5 → 6 → 4

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)

node4.next = node5
node5.next = node6

l2 = node4


# Print input lists
print("First Linked List:")
printList(l1)

print("Second Linked List:")
printList(l2)


# Add both linked lists
result = addTwoNumbers(l1, l2)


# Print result
print("Result:")
printList(result)