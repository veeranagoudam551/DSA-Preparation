class Solution:
    def countNodesinLoop(self, head):

        slow = head
        fast = head

        # Step 1: Detect loop
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            # Loop found
            if slow == fast:

                # Step 2: Count loop length
                count = 1
                current = slow.next

                while current != slow:
                    count += 1
                    current = current.next

                return count

        # No loop
        return 0