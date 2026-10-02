class Solution:
    def prefixToPostfix(self, s):

        stack = []

        # Scan from right to left
        for ch in s[::-1]:

            # Operand
            if ch.isalnum():
                stack.append(ch)

            # Operator
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()

                expression = operand1 + operand2 + ch

                stack.append(expression)

        return stack[-1]