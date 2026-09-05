class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        # Step 1: Detect the cycle
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # No cycle
        if fast is None or fast.next is None:
            return None

        # Step 2: Find starting point of cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow