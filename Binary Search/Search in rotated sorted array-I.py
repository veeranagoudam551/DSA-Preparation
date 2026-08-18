#Time Complexity: O(log n)
#Space Complexity: O(1)
def rotated_sorted(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        # Left half is sorted
        if arr[low]<=arr[mid]:
            if arr[low] <= target < arr[mid]:
                high=mid-1
            else:
                low=mid+1
                # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

target=int(input("Enter the target value:"))
arr=[4, 5, 6, 7, 0, 1, 2]
print(rotated_sorted(arr,target))