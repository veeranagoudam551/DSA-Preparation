class Solution:
    def subArrayRanges(self, nums):

        n = len(nums)

        # -------------------------
        # Sum of subarray minimums
        # -------------------------

        left_min = [0] * n
        right_min = [0] * n

        stack = []

        for i in range(n):

            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if stack:
                left_min[i] = i - stack[-1]
            else:
                left_min[i] = i + 1

            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                right_min[i] = stack[-1] - i
            else:
                right_min[i] = n - i

            stack.append(i)

        # -------------------------
        # Sum of subarray maximums
        # -------------------------

        left_max = [0] * n
        right_max = [0] * n

        stack = []

        for i in range(n):

            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            if stack:
                left_max[i] = i - stack[-1]
            else:
                left_max[i] = i + 1

            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                right_max[i] = stack[-1] - i
            else:
                right_max[i] = n - i

            stack.append(i)

        # -------------------------
        # Calculate answer
        # -------------------------

        minimum_sum = 0
        maximum_sum = 0

        for i in range(n):

            minimum_sum += nums[i] * left_min[i] * right_min[i]

            maximum_sum += nums[i] * left_max[i] * right_max[i]

        return maximum_sum - minimum_sum