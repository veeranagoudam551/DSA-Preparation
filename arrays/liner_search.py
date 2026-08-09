# Linear Search
# Approach: Linear Scan
# Time Complexity: O(n)
#space Complexity: O(1)
def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1


arr=[10, 20, 30, 40, 50,60]
target=int(input("Enter the target element: "))
print(linear_search(arr,target))
