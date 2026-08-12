def longest_palindrome(s):

    if len(s) == 0:
        return ""

    start = 0
    end = 0
    max_len = 0

    for i in range(len(s)):

        # Odd length palindrome
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l=l-1
            r=r+1

        if r - l - 1 > max_len:
            max_len = r - l - 1
            start = l + 1
            end = r - 1

        # Even length palindrome
        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l=l-1
            r=r+1

        if r - l - 1 > max_len:
            max_len = r - l - 1
            start = l + 1
            end = r - 1
    return s[start:end + 1]

s = "babad"
print(longest_palindrome(s))
