#Time: Complexity: O(n)
#Space: Complexity: O(1)
class Solution(object):
    def reverseList(self, head):

        prev = None
        current = head

        while current is not None:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev