# Problem: Left Rotate an Array by One Position
# Approach: Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

def rotate_array(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

arr=[10,20,50,30,60,40]
print(rotate_array(arr))
