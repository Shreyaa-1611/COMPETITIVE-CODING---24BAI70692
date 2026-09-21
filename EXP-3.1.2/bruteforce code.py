def solve(height, k, i):
    if i == 0:
        return 0

    best = float('inf')

    for j in range(max(0, i - k), i):
        cost = solve(height, k, j) + abs(height[i] - height[j])
        best = min(best, cost)

    return best


height = list(map(int, input("Enter heights: ").split()))
k = int(input("Enter maximum jump distance: "))

n = len(height)

print("Minimum cost:", solve(height, k, n - 1))