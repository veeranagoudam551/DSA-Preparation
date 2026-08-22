def row_with_max_ones(mat):
    max_ones = 0
    row_ans= -1
    for i in range(len(mat)):
        low=0
        high=len(mat[i])-1
        #find the first 1 in the row
        while low<=high:
            mid=(low+high)//2
            if mat[i][mid]==1:
                high=mid-1
            else:
                low=mid+1
        #count the number of 1's in the row
        count=len(mat[i])-low
        if count>max_ones:
            max_ones=count
            row_ans=i
    return row_ans  

mat = [
    [1, 1, 1],[0, 0, 1],[0, 0, 0]
]
print(row_with_max_ones(mat))