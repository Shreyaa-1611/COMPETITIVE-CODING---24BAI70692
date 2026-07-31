class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        temp = []

        while len(self.stack) > 1:
            temp.append(self.stack.pop())

        front = self.stack.pop()

        while temp:
            self.stack.append(temp.pop())

        return front

    def peek(self):
        temp = []

        while len(self.stack) > 1:
            temp.append(self.stack.pop())

        front = self.stack[-1]

        while temp:
            self.stack.append(temp.pop())

        return front

    def empty(self):
        return len(self.stack) == 0


q = MyQueue()

while True:
    print("\n1.Push 2.Pop 3.Peek 4.Empty 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        q.push(x)

    elif choice == 2:
        print("Output:", q.pop())

    elif choice == 3:
        print("Output:", q.peek())

    elif choice == 4:
        print("Output:", q.empty())

    elif choice == 5:
        break