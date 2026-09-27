class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum = 0
        answer = 0

        count = {0: 1}

        for num in nums:

            prefix_sum += num

            if prefix_sum - goal in count:
                answer += count[prefix_sum - goal]

            if prefix_sum not in count:
                count[prefix_sum] = 0

            count[prefix_sum] += 1

        return answer