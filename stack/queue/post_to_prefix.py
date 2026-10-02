class Solution:
    def postfixToPrefix(self, s):

        stack = []

        # Scan from left to right
        for ch in s:

            # Operand
            if ch.isalnum():
                stack.append(ch)

            # Operator
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                expression = ch + operand1 + operand2

                stack.append(expression)

        return stack[-1]