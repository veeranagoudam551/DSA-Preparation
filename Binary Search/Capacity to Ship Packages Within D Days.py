def ship_packages(weight, days):
    low=max(weight)
    high=sum(weight)
    while low<=high:
        mid=(low+high)//2
        current_weight=0
        days_needed=1
        for w in weight:
            if current_weight + w>mid:
                days_needed+=1
                current_weight=w
            else:
                current_weight+=w
        if days_needed>days:
            low=mid+1
        else:
            high=mid-1
    return low


weight=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days=int(input("Enter the number of days:"))
print(ship_packages(weight,days))