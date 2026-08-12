# Count the number of substrings with exactly k distinct characters
#Time Complexity: O(n)
#Space Complexity: O(n)

def at_most_k(s, k):
    left = 0
    count = {}
    result = 0

    for right in range(len(s)):
        # Add current character
        count[s[right]] = count.get(s[right], 0) + 1

        # If distinct characters are more than k,
        # move left until valid
        while len(count) > k:
            count[s[left]] -= 1

            if count[s[left]] == 0:
                del count[s[left]]

            left += 1

        # Count substrings ending at right
        result += right - left + 1

    return result


def count_substrings(s, k):
    return at_most_k(s, k) - at_most_k(s, k - 1)


s = "pqpqs"
k = 2

print(count_substrings(s, k))