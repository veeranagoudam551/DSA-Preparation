#Given two integers low and high, return the sum of all integers from low to high inclusive.
#Time Complexity:0(n)
#Space Complexity:0(1)
def sum(low,high):
    result=0
    for i in range(low,high+1):
        result=result+i
    return result
    
low=int(input("Enter the low value:"))
high=int(input("Enter the high value:"))
result=sum(low,high)
print("The Low value is",low,"and the High value is",high,"the total sum is",result)