# Function to find the maximum nesting depth of parentheses in a string
#Time Complexity: O(n) where n is the length of the string
#Space Complexity: O(1)
def max_depth(S):
    depth =0
    max_depth=0
    for i in S:
        if i=="(":
            depth=depth+1
            max_depth=max(max_depth,depth)
        elif i==")":
            depth=depth-1
    return max_depth

S = "()(())((()()))"
print(max_depth(S))