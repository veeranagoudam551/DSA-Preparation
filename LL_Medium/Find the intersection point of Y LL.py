class Solution:

    def getIntersectionNode(self, head1, head2):

        # Start pointers at both heads
        p1 = head1
        p2 = head2

        # Continue until both pointers meet
        while p1 != p2:

            # Move p1
            if p1 is None:
                p1 = head2
            else:
                p1 = p1.next

            # Move p2
            if p2 is None:
                p2 = head1
            else:
                p2 = p2.next

        # Return intersection node
        return p1

    