n=int(input("Enter the nth root of a number:"))
m=int(input("Enter the number to find the nth root of:"))
if m<2:
    print(m)
else:
    low=1
    high=m
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid**n==m:
            ans=mid
            break
        elif mid**n<m:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    print(ans)