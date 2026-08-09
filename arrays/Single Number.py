# Find the single number in an array where every other element appears twice
#Time Complexity: O(n)
#Space Complexity: O(1)

arr = [1,2,2,4,3,1,4]
result=0
for i in arr:
    result=result^i
print("The single number is:",result)