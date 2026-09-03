# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)


# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


head = node1


def find_middle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

    return slow


middle = find_middle(head)

print("Middle:", middle.data)