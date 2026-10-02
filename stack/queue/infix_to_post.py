class Solution:
    def infixToPostfix(self, s):

        stack = []
        result = ""

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

        for ch in s:

            # Operand
            if ch.isalnum():
                result += ch

            # Opening bracket
            elif ch == '(':
                stack.append(ch)

            # Closing bracket
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()

                stack.pop()

            # Operator
            else:
                while (stack and
                       stack[-1] != '(' and
                       precedence[stack[-1]] >= precedence[ch]):

                    result += stack.pop()

                stack.append(ch)

        # Pop remaining operators
        while stack:
            result += stack.pop()

        return result