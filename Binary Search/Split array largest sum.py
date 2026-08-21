def split_array(arr,k):
    arr.sort()
    if len(arr)<k:
        return -1

    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        sub_array=1
        current_sum=0
        for i in arr:
            if current_sum+i>mid:
                sub_array+=1
                current_sum=i
            else:
                current_sum+=i
        if sub_array>k:
            low=mid+1
        else:
            high=mid-1
    return low

arr=[10,20,30,40]
k=int(input("enter the number of students:"))
print(split_array(arr,k))