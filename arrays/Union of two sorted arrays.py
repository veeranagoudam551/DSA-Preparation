# Union of two sorted arrays
#Time Complexity: O(m+n)
#Space Complexity: O(m+n)
#In the worst case, there could be m + n unique elements.

arr1=[1, 2, 3, 4, 5]
arr2=[3, 4, 5, 6, 7]
union=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i] < arr2[j]:
        union.append(arr1[i])
        i=i+1
    elif arr1[i] > arr2[j]:
        union.append(arr2[j])
        j=j+1
    else:
        union.append(arr1[i])
        i=i+1
        j=j+1

# Append any remaining elements from either array
union.extend(arr1[i:])
union.extend(arr2[j:])

print("Union of two sorted arrays is:", union)