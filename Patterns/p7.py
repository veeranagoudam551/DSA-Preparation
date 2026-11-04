class Solution():
  def pattern7(self,n):
    for i in range(1,n+1):

      for j in range(n-i):
        print(" ",end="")
      for j in range(2*i-1):
        print("*",end="")
      print()
obj=Solution()
obj.pattern7(4)

#TC:O(n^2)
#SC:O(1)