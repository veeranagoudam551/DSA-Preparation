#TC = O(n^2)
#SC = O(1)

arr=[1,6,2,10,3,5]
target=7
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            print("Pair found at index",i,"and",j)
            print("The pair is (",arr[i],",",arr[j],")")
            break
    else:
        continue
    break

#But notice:

##The else belongs to the inner for loop.

##A for loop's else runs only if the loop finishes normally (without a break).

##Since the inner loop ended because of break, the else is skipped.

##Execution continues to the next line:


##HASHING
arr=[1,7,6,10,3.5]
target=7
n=len(arr)
hash_map={}
for i in range(n):
    remaining=target-arr[i]
    if remaining in hash_map:
        print("Pair found at index",hash_map[remaining], "and", i)
        print("The pair is (", remaining, ",", arr[i], ")")
        break
    hash_map[arr[i]] = i

#TC = O(n)
#SC = O(n)