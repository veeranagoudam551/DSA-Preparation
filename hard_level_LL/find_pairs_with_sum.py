class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def find_pairs(head, target):

    pairs = []

    # Empty list
    if head is None:
        return pairs

    # Find last node
    left = head
    right = head

    while right.next is not None:
        right = right.next

    # Two pointer approach
    while left != right and left != right.next:

        total = left.data + right.data

        if total == target:

            pairs.append((left.data, right.data))

            left = left.next
            right = right.prev

        elif total < target:

            # Need a bigger sum
            left = left.next

        else:

            # Need a smaller sum
            right = right.prev

    return pairs


def print_pairs(pairs):

    for pair in pairs:
        print(pair)


# -------------------------
# Create DLL
# -------------------------

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(6)
node6 = Node(8)

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

target = 10

pairs = find_pairs(head, target)

print("Pairs:")
print_pairs(pairs)