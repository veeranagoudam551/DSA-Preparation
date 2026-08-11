# Convert Roman numerals to integers
#Time Complexity: O(n)
#Space Complexity: O(1)
def roman_to_integer(s):
    roman_dict={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            total = total-roman_dict[s[i]]
        else:
            total = total + roman_dict[s[i]]

    return total

s = "XLII"
print(roman_to_integer(s))

