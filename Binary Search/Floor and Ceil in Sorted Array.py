#Time Complexity: O(logn)
#Space Complexity: O(1)
def floor_ceil(arr,target):
    low=0
    high=len(arr)-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            floor=arr[mid]
            ceil=arr[mid]
            return [floor,ceil]
        elif arr[mid]<target:
            floor=arr[mid]
            low=mid+1
        else:
            ceil=arr[mid]
            high=mid-1
    return [floor,ceil]
target=int(input("Enter the target value: "))
arr=[1,3,5,6,7,8,9]
print(floor_ceil(arr,target))