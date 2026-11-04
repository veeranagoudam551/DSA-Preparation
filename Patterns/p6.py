class Solution():
  def pattern6(self,n):
    for i in range(n):
      for j in range(1,n-i+1):
        print(j,end="")
      print()
obj=Solution()
obj.pattern6(5)

#TC:O(n^2)
#SC:O(1)


