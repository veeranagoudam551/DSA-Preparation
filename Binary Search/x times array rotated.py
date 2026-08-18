def findRotations(arr, n):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low+high)//2

            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                 high = mid
        return low
arr=[4, 5, 6, 7, 0, 1, 2]
n=len(arr)
print(findRotations(arr, n))