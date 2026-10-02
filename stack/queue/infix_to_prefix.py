class Solution:
    def infixToPrefix(self, s):

        # Step 1: Reverse the expression
        s = s[::-1]

        # Step 2: Swap brackets
        s = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                s[i] = ')'
            elif s[i] == ')':
                s[i] = '('

        s = ''.join(s)

        stack = []
        result = ""

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

        # Step 3: Infix to Postfix
        for ch in s:

            if ch.isalnum():
                result += ch

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()

                stack.pop()

            else:
                while (stack and
                       stack[-1] != '(' and
                       precedence[stack[-1]] > precedence[ch]):

                    result += stack.pop()

                stack.append(ch)

        while stack:
            result += stack.pop()

        # Step 4: Reverse postfix
        return result[::-1]