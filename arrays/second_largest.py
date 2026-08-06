# Problem: Second largest Element in an Array
# Approach: Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    largest=float('-inf')
    second=float('-inf')
    
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second = num
    if second==float('-inf'):
        return -1
    
    return second


arr = [10, 20, 50, 30, 50,40]
print("Second_largest is",second_largest(arr))