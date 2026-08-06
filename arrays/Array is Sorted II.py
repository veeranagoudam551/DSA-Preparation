# Problem: is sorted Element in an Array
# Approach: Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

def issorted(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False

    return True

arr = [10,20,30,40,50,60]
print(issorted(arr))