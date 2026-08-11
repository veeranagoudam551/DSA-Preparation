# Function to find the longest common prefix among an array of strings
#Time Complexity  : O(n × m)
#Space Complexity : O(m)
#We compare the prefix with each string, and in the worst case we may check up to m characters for each of the n strings.
def common_prefix(s):
    if not s:
        return ""
    prefix =s[0]
    for i in s:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
    return prefix

s=["flower","flow","flight","fly"]
print(common_prefix(s))