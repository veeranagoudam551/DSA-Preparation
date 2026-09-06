class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(left, right):

    # Dummy node
    dummy = Node(0)
    current = dummy

    # Compare and merge
    while left is not None and right is not None:

        if left.data < right.data:

            current.next = left
            left = left.next

        else:

            current.next = right
            right = right.next

        current = current.next

    # Attach remaining nodes
    if left is not None:
        current.next = left
    else:
        current.next = right

    return dummy.next


def sortList(head):

    # Base case
    if head is None or head.next is None:
        return head

    # Find middle
    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:

        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split the list
    prev.next = None

    # Sort left half
    left = sortList(head)

    # Sort right half
    right = sortList(slow)

    # Merge both sorted halves
    return merge(left, right)


# Create Linked List
node1 = Node(4)
node2 = Node(2)
node3 = Node(1)
node4 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


# Sort Linked List
head = sortList(head)


# Print Linked List
current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")