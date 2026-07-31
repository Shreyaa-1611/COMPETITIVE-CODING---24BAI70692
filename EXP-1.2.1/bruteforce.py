def searchInsert(nums, target):

    for i in range(len(nums)):
        if nums[i] >= target:
            return i

    return len(nums)


nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

print("Output:", searchInsert(nums, target))