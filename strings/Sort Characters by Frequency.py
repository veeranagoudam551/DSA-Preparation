#Time complexity : O(nlogn)
#Space complexity : O(n)
def sort_characters_by_frequency(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    result = sorted(count.keys(), key=lambda x: (-count[x], x))
    return result

s = "tree"
print(sort_characters_by_frequency(s))


# Time Complexity
# 1. Counting characters
# for char in s:
# We visit every character once.
# O(n)
# 2. Sorting unique characters
# sorted(count.keys(), ...)
# There are only k unique characters.
# Sorting takes:
# O(k log k)
# Total
# O(n) + O(k log k)
# So:
# TC = O(n + k log k)
# Since k ≤ n, this can be simplified to:
# TC = O(n log n)