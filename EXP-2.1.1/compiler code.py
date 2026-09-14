def subsets(nums):
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


nums = list(map(int, input("Enter array elements: ").split()))

print("Output:", subsets(nums))