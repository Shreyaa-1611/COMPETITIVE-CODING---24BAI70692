def combinationSum(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break

            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

print("Output:", combinationSum(candidates, target))