n = int(input("Enter number of stairs: "))

if n <= 2:
    print("Number of ways:", n)
else:
    a = 1
    b = 2

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    print("Number of ways:", b)