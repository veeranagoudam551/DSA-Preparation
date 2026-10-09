class Solution:
    def canJump(self, nums):
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= len(nums) - 1:
                return True

        return True


# Take input
nums = list(map(int, input("Enter array elements: ").split()))

# Call the function
obj = Solution()
answer = obj.canJump(nums)

# Print the result
print(answer)