n=int(input("Enter the number to find the square root of:"))
if n<2:
    print(n)
else:
    low=1
    high=n
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            ans=mid
            break
        elif mid*mid<n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    print(ans)