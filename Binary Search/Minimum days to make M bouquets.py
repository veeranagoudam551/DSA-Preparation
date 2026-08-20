# TIME COMPLEXITY: O(n log(max(arr) - min(arr)))
#SPACE COMPLEXITY: O(1)
# 
def min_days(arr, m, k):
    if m * k > len(arr):
        return -1
    low = min(arr)
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2

        bouquets = 0
        flowers = 0

        for day in arr:
            if day <= mid:
                flowers += 1

                if flowers == k:
                    bouquets += 1
                    flowers = 0

            else:
                flowers = 0

        if bouquets >= m:
            high = mid - 1
        else:
            low = mid + 1

    return low
arr=[7, 7, 7, 7, 13, 11, 12, 7]
m=int(input("Enter the number of bouquets:"))
k=int(input("Enter the number of flowers in each bouquet:"))
print(min_days(arr, m, k))