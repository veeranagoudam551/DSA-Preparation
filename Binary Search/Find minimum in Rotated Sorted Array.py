#Time Complexity: O(log n)
#space Complexity: O(1)
def minimum_sorted(arr):
    low=0
    high=len(arr)-1
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2
        ans=min(ans,arr[mid])
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans

arr=[4, 5, 6, 0, 1, 2, 3]
print(minimum_sorted(arr))