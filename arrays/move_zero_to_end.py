# Move all zeros to the end of the array
#Time Complexity: O(n)
#Space Complexity: O(1)
#O(n) + O(n)
#= O(2n)
#= O(n)

def move_zeroto_end(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[j]=arr[i]
            j=j+1
    while j<n:
            arr[j]=0
            j=j+1
    return arr





arr=[0,1,0,3,12]
print(move_zeroto_end(arr))
