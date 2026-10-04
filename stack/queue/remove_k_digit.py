class Solution(object):
    def removeKdigits(self, num, k):

        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If k is still remaining
        while k > 0:
            stack.pop()
            k -= 1

        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')

        # If nothing remains
        if result == "":
            return "0"

        return result