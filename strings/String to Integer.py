#Time Complexity: O(n)
#Space Complexity: O(1)
def myAtoi(s):
    i=0
    n=len(s)
    #Remove Leading whitespaces
    while i<n and s[i]==' ':
        i=i+1
    #check sign
    sign=1
    if i<n and s[i]=='+':
        sign=1
        i=i+1
    elif i<n and s[i]=='-':
        sign=-1
        i=i+1
    #convert to interger
    num=0
    while i<n and s[i].isdigit():
        num=num*10+int(s[i])
        i=i+1
    #apply sign
    num=num*sign

    # Step 4: Clamp to 32-bit range
    if num < -2147483648:
        return -2147483648

    if num > 2147483647:
        return 2147483647

    return num

s = " -12345"
print(myAtoi (s))



# Skip spaces → O(n)
# Check sign → O(1)
# Read digits → O(n)
# Range checks → O(1)
