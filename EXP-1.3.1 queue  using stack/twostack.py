class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):

        if not self.output:

            while self.input:
                self.output.append(self.input.pop())

        return self.output.pop()

    def peek(self):

        if not self.output:

            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0


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