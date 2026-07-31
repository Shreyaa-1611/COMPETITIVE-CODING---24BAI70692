class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)

        pre = [-1] * n
        post = [n] * n
        st = []

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                post[st.pop()] = i

            pre[i] = st[-1] if st else -1
            st.append(i)

        ans = 0

        for i in range(n):
            width = post[i] - pre[i] - 1
            ans = max(ans, heights[i] * width)

        return ans