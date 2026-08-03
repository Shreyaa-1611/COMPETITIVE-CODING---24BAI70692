class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def hasCycle(head):

    visited = []

    while head:

        if head in visited:
            return True

        visited.append(head)
        head = head.next

    return False


# Creating a sample linked list with a cycle
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

# Creating cycle
head.next.next.next.next = head.next

print("Output:", hasCycle(head))