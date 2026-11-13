class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            best = max(best, self.largest_in_histogram(heights))
        return best

    def largest_in_histogram(self, heights):
        stack = []          # indices, heights increasing
        best = 0
        for i in range(len(heights) + 1):
            h = heights[i] if i < len(heights) else 0   # sentinel 0 flushes the stack
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, height * width)
            stack.append(i)
        return best 