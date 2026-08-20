def smallest_division(arr,threshold):
    low=1
    high=max(arr)
    while low<=high:
        mid=(low+high)//2
        total=0
        for i in arr:
            total +=(i + mid -1)//mid
        if total>threshold:
            low=mid+1
        else:
            high=mid-1
    return low

arr=[1, 2, 3, 4, 5]
threshold=int(input("Enter the threshold:"))
print(smallest_division(arr,threshold))