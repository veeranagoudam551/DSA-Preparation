class Solution:
    def deleteMiddle(self, head):

        # If only one node
        if head is None or head.next is None:
            return None

        prev = None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head