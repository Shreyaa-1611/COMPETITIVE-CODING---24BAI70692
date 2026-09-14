def findDuplicate(nums):

    # Phase 1: Find intersection point
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Phase 2: Find entrance of cycle
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# -------- USER INPUT --------

nums = list(map(int, input("Enter array elements: ").split()))

answer = findDuplicate(nums)

print("Duplicate Number:", answer)