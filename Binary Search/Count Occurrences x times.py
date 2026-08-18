#Time Complexity:0(logn)
#space Complexity:0(1)
def first_last_occrurrence(arr,target):
    first=-1
    last=-1
    #lower bound
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            first=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    #upper bound
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            last=mid
            low=mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1 
    if first==-1 and last==-1:
        return 0
    else:
        return last-first+1      

target=int(input("Enter the target value:"))
arr=[1, 2, 2, 2, 3, 4, 4, 5,6]
print(first_last_occrurrence(arr,target))