#Time Complexity: O(logn)
#Space Complexity: O(1)
def Upper_bound(arr,target):
    low=0
    ans=len(arr)
    high=len(arr)-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    
target=int(input("Enter the target value to search:"))
arr= [1,2,2,3,4,5,5,6]
print(Upper_bound(arr,target))

#Find the first index where the array value is greater than the target.