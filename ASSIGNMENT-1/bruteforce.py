def search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


nums = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))

print("Output:", search(nums, target))