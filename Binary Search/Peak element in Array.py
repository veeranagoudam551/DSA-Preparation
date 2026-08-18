def peak_element(arr,n):
    low=0
    high=(n)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[mid+1]:
            high=mid
        else:
            low=mid+1
    return low

arr=[1, 3, 20, 25, 1, 4]
n=len(arr)
print(peak_element(arr,n))