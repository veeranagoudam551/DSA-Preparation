#Time Complexity: O(log n)  Every time the loop runs, we cut the search area in half.
#Space Complexity: O(1)   Because we only use a few variables:
 def search_index(arr,target):
    low=0
    high=len(arr)-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

target=int(input("Enter the target value to search:"))
arr= [-1,0,3,5,9,12]
print(search_index(arr, target))