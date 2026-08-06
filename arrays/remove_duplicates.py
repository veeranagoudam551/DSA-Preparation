# Problem: Remove duplicates from a sorted array
# Approach: Two Pointer Technique
# Time Complexity: O(n)
# Space Complexity: O(1)


def remove_duplicates(arr):
    n=len(arr)
    if n == 0:
        return 0

    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            i = i + 1
            arr[i] = arr[j]
    return i+1

arr = [1, 1, 2, 2, 3, 4, 4]
length=remove_duplicates(arr)
print("Unique Elements are ",length)
print("Array after removing duplicates:", arr[:length])
