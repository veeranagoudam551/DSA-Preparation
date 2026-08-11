# Rotate String
#Time Complexity: O(n)
#Space Complexity: O(n)
def rotate_string(s,goal):
    if len(s) != len(goal):
        return False
    return goal in (s+s)

s = "abcde"
goal = "cdeab"
print(rotate_string(s,goal))


#creates a new string of size 2n.   s + s
#goal in (s + s) → substring search → commonly treated as O(n) for this DSA problem.