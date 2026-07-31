from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


stack = MyStack()

while True:
    print("\n1.Push 2.Pop 3.Top 4.Empty 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        stack.push(x)

    elif choice == 2:
        print("Output:", stack.pop())

    elif choice == 3:
        print("Output:", stack.top())

    elif choice == 4:
        print("Output:", stack.empty())

    elif choice == 5:
        break