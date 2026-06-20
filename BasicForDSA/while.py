#Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
#Time complexity:0(1)
#Space complexity:0(1)
d=int(input("enter the d value:"))
n=0
total=0
current=d
while n<50:
    total=total+current
    current=current+10
    n=n+1
print(total)
    
    