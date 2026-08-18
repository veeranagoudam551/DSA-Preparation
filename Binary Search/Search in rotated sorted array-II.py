def sorted_rotation(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        # handle duplicates
        if arr[low]==arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        # left half is sorted
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        # right half is sorted
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False



target=int(input("Enter the target value:"))
arr=[7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
print(sorted_rotation(arr,target))