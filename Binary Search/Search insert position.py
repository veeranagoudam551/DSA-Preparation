#Time Complexity: O(logn)
#Space Complexity: O(1)
def insert_position(arr,target):
    low=0
    ans=len(arr)
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans = mid
            high=mid-1
        else:
            low=mid+1
    return ans


target=int(input("Enter the target value to insert: "))
arr=[1,3,5,6]
print(insert_position(arr,target))
