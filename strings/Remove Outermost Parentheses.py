#remove the outermost parentheses from a valid parentheses string
#Time Complexity: O(n)
#space Complexity: O(n)

def remove_outer_parentheses(s):
    count = 0
    result = ""
    for char in s:
        if char == "(":
            if count > 0:
                result += "("
            count += 1
        else:
            count -= 1
            if count > 0:
                result += ")"

    return result

s = "(()())(())"
print(remove_outer_parentheses(s))