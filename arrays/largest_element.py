# Problem: Largest Element in an Array
# Approach: Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

def largest_num(arr):
    n=len(arr)
    max_val=arr[0]
    for i in range(1,n):
        if arr[i]>max_val:
            max_val=arr[i]
    return max_val
arr=[10,20,50,30,40,60]
print("largest Element",largest_num(arr))
