#Time complexity:0(log n)
#Space complexity:0(1)
def lower_bound(arr,target):
    low=0
    ans=len(arr)
    high=len(arr)-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    
target=int(input("Enter the target value to search:"))
arr= [1,2,2,3,4,5,5,6]
print(lower_bound(arr,target))
