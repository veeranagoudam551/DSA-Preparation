class Solution(object):
    def numberOfSubarrays(self, nums, k):

        odd_count = 0
        answer = 0

        count = {0: 1}

        for num in nums:

            # Count odd numbers
            if num % 2 == 1:
                odd_count += 1

            # We need previous prefix with
            # odd_count - k
            if odd_count - k in count:
                answer += count[odd_count - k]

            # Store current odd_count
            if odd_count not in count:
                count[odd_count] = 0

            count[odd_count] += 1

        return answer