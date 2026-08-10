#Time Complexity: O(n)
#Space Complexity: O(n)
def reverse_word(s):
    words =s.split()
    reverse_words = words[::-1]
    return " ".join(reverse_words)

s="The Sky Is Blue"
print(reverse_word(s))

#[start : stop : step]