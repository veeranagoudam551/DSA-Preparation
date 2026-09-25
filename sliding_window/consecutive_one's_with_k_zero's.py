class Solution(object):
    def longestOnes(self, nums, k):

        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):

            # If current element is 0
            if nums[right] == 0:
                zeros += 1

            # Too many zeros, shrink the window
            while zeros > k:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            # Current window is valid
            current_length = right - left + 1

            max_length = max(max_length, current_length)

        return max_length