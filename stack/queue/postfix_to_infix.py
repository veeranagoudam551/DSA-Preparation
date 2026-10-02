class Solution:
    def postfixToInfix(self, s):

        stack = []

        for ch in s:

            # Operand
            if ch.isalnum():
                stack.append(ch)

            # Operator
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                expression = "(" + operand1 + ch + operand2 + ")"

                stack.append(expression)

        return stack[-1]