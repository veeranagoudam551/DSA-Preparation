class Solution:
    def nextGreaterElements(self, arr):

        n = len(arr)

        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):

            current = arr[i % n]

            while stack and stack[-1] <= current:
                stack.pop()

            if i < n and stack:
                result[i] = stack[-1]

            stack.append(current)

        return result