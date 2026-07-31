def search(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


nums = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))

print("Output:", search(nums, target))