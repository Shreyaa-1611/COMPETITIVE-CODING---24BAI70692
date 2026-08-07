class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = []
        even = []

        temp = head
        position = 1

        while temp:
            if position % 2 == 1:
                odd.append(temp.val)
            else:
                even.append(temp.val)

            temp = temp.next
            position += 1

        values = odd + even

        dummy = ListNode(0)
        curr = dummy

        for value in values:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next