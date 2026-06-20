#Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

#Time Complexity: O(n)
#Space Complexity: O(1)
arr=[1,2,3,4,5]
left=0
right=4
while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left=left+1
    right=right-1
print(arr)
    