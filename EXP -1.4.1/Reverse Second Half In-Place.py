class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None

    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    first = head
    second = prev

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


arr = list(map(int, input("Enter linked list elements: ").split()))

dummy = ListNode()
curr = dummy

for x in arr:
    curr.next = ListNode(x)
    curr = curr.next

print("Output:", isPalindrome(dummy.next))