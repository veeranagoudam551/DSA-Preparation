class Solution(object):
    def rotateRight(self, head, k):

        if head is None or head.next is None:
            return head

        # Find length and last node
        length = 1
        current = head

        while current.next is not None:
            current = current.next
            length += 1

        # Avoid unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make the list circular
        current.next = head

        # Find the new last node
        steps = length - k
        current = head

        for i in range(steps - 1):
            current = current.next

        # New head
        new_head = current.next

        # Break the circle
        current.next = None

        return new_head