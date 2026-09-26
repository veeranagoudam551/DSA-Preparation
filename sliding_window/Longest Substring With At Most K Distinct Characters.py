class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):

            # Add current character
            if s[right] not in count:
                count[s[right]] = 0

            count[s[right]] += 1

            # If more than k distinct characters, shrink window
            while len(count) > k:
                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

            # Update maximum length
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length