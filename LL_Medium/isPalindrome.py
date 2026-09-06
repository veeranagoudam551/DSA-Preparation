def isPalindrome(head):

    # Step 1: Find middle
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next


    # Step 2: Reverse from middle
    prev = None
    current = slow

    while current is not None:

        next_node = current.next
        current.next = prev

        prev = current
        current = next_node