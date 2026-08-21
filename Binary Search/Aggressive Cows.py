def Aggressive_cows(arr,k):
    arr.sort()
    low=0
    high=arr[-1]-arr[0]
    while low<=high:
        mid=(low+high)//2
        cow=1
        last_position=arr[0]

        for i in range(1,len(arr)):
            if arr[i]-last_position>=mid:
                cow=cow+1
                last_position=arr[i]

        if cow>=k:
            low=mid+1
        else:
            high=mid-1
    return high

arr=[0,3,4,7,9,10]
k=int(input("Enter the number of cows:"))
print(Aggressive_cows(arr,k))