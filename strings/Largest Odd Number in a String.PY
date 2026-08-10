def largest_odd_number(s):
    # Initialize an empty string to store the largest odd number
    largest_odd =""
    # iterate through the string in reverse order
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 !=0:
            largest_odd = s[:i+1].lstrip("0")
            break
    return largest_odd
s="0214638"
print(largest_odd_number(s))