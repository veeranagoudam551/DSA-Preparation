class Solution():
  def pattern8(self,n):
    for i in range(1,n+1):
      for j in range(i-1):
        print(" ",end="")
      for j in range(2*(n-i)+1):
        print("*",end="")
      print()
obj=Solution()
obj.pattern8(4)

#TC:O(n^2)
#SC:O(1)