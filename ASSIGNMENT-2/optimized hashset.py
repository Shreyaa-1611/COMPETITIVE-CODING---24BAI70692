class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    visited = set()

    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False


arr = list(map(int, input("Enter linked list elements: ").split()))
pos = int(input("Enter cycle position (-1 for no cycle): "))

nodes = [ListNode(x) for x in arr]

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

if pos != -1:
    nodes[-1].next = nodes[pos]

head = nodes[0]

print("Output:", hasCycle(head))