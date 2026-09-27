class Solution(object):
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            left = 0
            count = {}
            answer = 0

            for right in range(len(nums)):

                # Add current number
                if nums[right] not in count:
                    count[nums[right]] = 0

                count[nums[right]] += 1

                # Too many distinct numbers
                while len(count) > k:

                    count[nums[left]] -= 1

                    if count[nums[left]] == 0:
                        del count[nums[left]]

                    left += 1

                # Count valid subarrays ending at right
                answer += right - left + 1

            return answer

        return atMost(k) - atMost(k - 1)