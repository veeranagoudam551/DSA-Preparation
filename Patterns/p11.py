class Solution():
  def pattern11(self,n):
    for i in range(1,n+1):
      for j in range(i):
       print((i+j)%2,end=" ")
      print()
obj=Solution()
obj.pattern11(4)

# TC: O(n²)
# SC: O(1)