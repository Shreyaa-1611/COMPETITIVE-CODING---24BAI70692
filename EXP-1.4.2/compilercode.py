class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def oddEvenList(head):
    if head is None or head.next is None:
        return head

    odd = []
    even = []

    temp = head
    position = 1

    while temp:
        if position % 2 == 1:
            odd.append(temp.data)
        else:
            even.append(temp.data)

        temp = temp.next
        position += 1

    # Combine odd positions followed by even positions
    result = odd + even

    # Create new linked list
    dummy = Node(0)
    current = dummy

    for value in result:
        current.next = Node(value)
        current = current.next

    return dummy.next


# Input
n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter elements: ").split()))

# Create linked list
head = Node(values[0])
temp = head

for i in range(1, n):
    temp.next = Node(values[i])
    temp = temp.next

# Apply function
head = oddEvenList(head)

# Output
print("Output:", end=" ")

temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next