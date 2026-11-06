class Solution():
  def pattern10(self,n):
    for i in range(1,n+1):
      for j in range(i):
        print("*",end="")
      print()
    for i in range(1,n+1):
      for j in range(n-i):
        print("*",end="")
      print()

    
obj=Solution()
obj.pattern10(4)

# TC: O(n²)
# SC: O(1)