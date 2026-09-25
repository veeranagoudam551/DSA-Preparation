class Solution(object):
    def lengthOfLongestSubstring(self, s):

        left = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):

            # If duplicate exists, remove from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character
            char_set.add(s[right])

            # Calculate window length
            current_length = right - left + 1

            # Update maximum
            max_length = max(max_length, current_length)

        return max_length