class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):

    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values == values[::-1]


arr = list(map(int, input("Enter linked list elements: ").split()))

dummy = ListNode()
curr = dummy

for x in arr:
    curr.next = ListNode(x)
    curr = curr.next

print("Output:", isPalindrome(dummy.next))