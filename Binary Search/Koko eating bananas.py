#Time Complexity: O(n × log(max(arr))) The binary search runs over possible speeds from 1 to max(arr) → O(log(max(arr)))
#For every speed, you loop through all piles → O(n)
#space Complexity: O(1)

def koko_banana(arr,h):
    low=1
    high=max(arr)
    while low<=high:
        mid=(low+high)//2
        total=0
        for i in arr:
            total += (i + mid - 1) // mid
        if total>h:
            low=mid+1
        else:
            high=mid-1
    return low

h=int(input("enter the deadline in hours:"))
arr=[3,6,7,11]
print(koko_banana(arr,h))