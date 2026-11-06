class Solution:
    def pattern9(self, n):
        # Upper pyramid
        for i in range(1, n+1):
            for j in range(n-i):
                print(" ", end="")
            for j in range(2*i-1):
                print("*", end="")
            print()

        # Inverted pyramid
        for i in range(1, n+1):
            for j in range(i-1):
                print(" ", end="")
            for j in range(2*(n-i)+1):
                print("*", end="")
            print()


obj = Solution()
obj.pattern9(4)

#TC: O(n²)
#SC: O(1)