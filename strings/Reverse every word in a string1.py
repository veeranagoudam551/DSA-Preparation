def reverse_words(s):
    words = s.split()
    reverse_words = words[::-1]
    return " ".join(reverse_words)


s = "welcome to the jungle"
print(reverse_words(s))