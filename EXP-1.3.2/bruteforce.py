def largestRectangleArea(heights):

    n = len(heights)
    max_area = 0

    for i in range(n):

        min_height = heights[i]

        for j in range(i, n):

            min_height = min(min_height, heights[j])
            area = min_height * (j - i + 1)

            max_area = max(max_area, area)

    return max_area


heights = list(map(int, input("Enter histogram heights: ").split()))

print("Output:", largestRectangleArea(heights))