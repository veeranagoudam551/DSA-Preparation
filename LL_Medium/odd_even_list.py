def oddEvenList(head):

    if head is None:
        return None

    odd = head
    even = head.next

    evenHead = head.next

    while even is not None and even.next is not None:

        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = evenHead

    return head