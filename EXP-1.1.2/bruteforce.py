def productExceptSelf(nums):
    n = len(nums)
    answer = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        answer.append(product)

    return answer


nums = list(map(int, input("Enter array elements: ").split()))

print("Output:", productExceptSelf(nums))