class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        need = {}

        for ch in t:
            if ch not in need:
                need[ch] = 0
            need[ch] += 1

        window = {}

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        min_start = 0

        for right in range(len(s)):

            ch = s[right]

            if ch not in window:
                window[ch] = 0

            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:

                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start:min_start + min_length]