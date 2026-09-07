class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Function to sort 0's, 1's and 2's
def sort012(head):

    # Empty list
    if head is None:
        return None

    # Create dummy nodes
    zero_dummy = Node(-1)
    one_dummy = Node(-1)
    two_dummy = Node(-1)

    # Tail pointers
    zero_tail = zero_dummy
    one_tail = one_dummy
    two_tail = two_dummy

    # Traverse original list
    current = head

    while current is not None:

        # If current node contains 0
        if current.data == 0:

            zero_tail.next = current
            zero_tail = zero_tail.next

        # If current node contains 1
        elif current.data == 1:

            one_tail.next = current
            one_tail = one_tail.next

        # If current node contains 2
        else:

            two_tail.next = current
            two_tail = two_tail.next

        # Move current pointer
        current = current.next

    # Connect 0's list to 1's list
    # If there are no 1's, connect directly to 2's
    zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next

    # Connect 1's list to 2's list
    one_tail.next = two_dummy.next

    # End the final list
    two_tail.next = None

    # Return actual head
    return zero_dummy.next


# Function to print Linked List
def printList(head):

    current = head

    while current is not None:

        print(current.data, end=" → ")
        current = current.next

    print("None")


# --------------------------------
# CREATE LINKED LIST
# Input: 1 → 2 → 0 → 1 → 2 → 0
# --------------------------------

node1 = Node(1)
node2 = Node(2)
node3 = Node(0)
node4 = Node(1)
node5 = Node(2)
node6 = Node(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1


# Print original list
print("Original Linked List:")
printList(head)


# Sort the list
head = sort012(head)


# Print sorted list
print("Sorted Linked List:")
printList(head)