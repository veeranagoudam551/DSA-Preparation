# Find the maximum number of consecutive 1's in a binary array
#Time Complexity: O(n)
#Space Complexity: O(1)
nums=[1,1,0,0,1,1,1,0,1,1]
n=len(nums)
count=0
MAX=0
for i in range(n):
    if nums[i]==1:
        count=count+1
        if count>MAX:
            MAX=count
    else:
        count=0
print("the maximum consecutive ones are:",MAX)