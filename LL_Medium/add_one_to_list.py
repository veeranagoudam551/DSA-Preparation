class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------------------------
# RECURSIVE HELPER FUNCTION
# ---------------------------------

def addOneHelper(node):

    # Base case:
    # We reached after the last node
    if node is None:
        return 1

    # Go to the next node first
    carry = addOneHelper(node.next)

    # While returning back, add carry
    node.data= node.data + carry

    if node.data <10:
        return 0
    else:
        node.data = 0
        return 1

    

# ---------------------------------
# MAIN FUNCTION
# ---------------------------------

def addOne(head):

    # Start recursion
    carry = addOneHelper(head)

    # If carry is still 1
    # Example: 999 + 1 = 1000
    if carry == 1:

        # Create new node
        newNode = Node(1)

        # Connect new node to old head
        newNode.next = head

        # New node becomes head
        head = newNode

    return head


# ---------------------------------
# PRINT FUNCTION
# ---------------------------------

def printList(head):

    current = head

    while current is not None:

        print(current.data, end=" → ")
        current = current.next

    print("None")


# ---------------------------------
# CREATE LINKED LIST
# 9 → 9 → 9 → 9
# ---------------------------------

node1 = Node(9)
node2 = Node(9)
node3 = Node(9)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


# ---------------------------------
# PRINT ORIGINAL LIST
# ---------------------------------

print("Original Number:")
printList(head)


# ---------------------------------
# ADD 1
# ---------------------------------

head = addOne(head)


# ---------------------------------
# PRINT RESULT
# ---------------------------------

print("After Adding 1:")
printList(head)