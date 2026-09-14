class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def solve(index, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target or index == len(candidates):
                return

            # Include current element
            current.append(candidates[index])
            solve(index, current, total + candidates[index])
            current.pop()

            # Skip current element
            solve(index + 1, current, total)

        solve(0, [], 0)
        return result