#Time Complexity: O(n^2)
#Space Complexity: O(1)
def longest_subarray_with_sum_k(arr,k):
    n=len(arr)
    max_length=0
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum=current_sum+arr[j]
            if current_sum==k:
                max_length=max(max_length,j-i+1)
    return max_length

arr=[1, 2, 3, 1, 1, 1, 1]
k=int(input("Enter the value of k:"))
print("The longest subarray with sum k is:", longest_subarray_with_sum_k(arr, k))