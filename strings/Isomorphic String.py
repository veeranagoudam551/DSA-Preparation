# Check if two strings are isomorphic
#Time Complexity  : O(n)
#Space Complexity : O(n)
def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False

        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False

        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s

    return True
   

s="egg"
t="add"
print(is_isomorphic(s,t))