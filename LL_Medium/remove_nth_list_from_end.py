class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Remove node
        slow.next = slow.next.next

        return dummy.next