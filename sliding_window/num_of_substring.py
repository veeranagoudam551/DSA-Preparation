class Solution(object):
    def numberOfSubstrings(self, s):
        last_a = -1
        last_b = -1
        last_c = -1

        answer = 0

        for right in range(len(s)):

            if s[right] == 'a':
                last_a = right

            elif s[right] == 'b':
                last_b = right

            else:
                last_c = right

            # If all three characters have appeared
            if last_a != -1 and last_b != -1 and last_c != -1:
                answer += min(last_a, last_b, last_c) + 1

        return answer