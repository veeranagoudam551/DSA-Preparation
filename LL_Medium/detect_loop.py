#Time Complexity: O(n)
#Space Complexity:O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create a loop
node5.next = node3


head = node1


def detect_loop(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


print(detect_loop(head))