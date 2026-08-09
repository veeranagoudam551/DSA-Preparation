#Expected sum − Actual sum = Missing number
#Time Complexity: O(n)
#Space Complexity: O(1)
#sum(arr) → O(n) because Python checks every element
arr=[0, 2, 3, 4,]
n=len(arr)
expected_sum=n*(n+1)//2
actual_sum=sum(arr)
missing_number=expected_sum-actual_sum
print("The missing number is:", missing_number)