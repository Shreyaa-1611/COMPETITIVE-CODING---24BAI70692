def addDigits(num):

    if num == 0:
        return 0

    return 1 + (num - 1) % 9


# -------- USER INPUT --------

num = int(input("Enter a number: "))

answer = addDigits(num)

print("Single Digit:", answer)