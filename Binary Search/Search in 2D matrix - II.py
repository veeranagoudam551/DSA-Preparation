# Search in 2D Matrix - II
#Time Complexity: O(rows + cols)
#Space Complexity: O(1)
def matrix_search(matrix,target):
    if not matrix or not matrix[0]:
        return False
    rows=len(matrix)
    cols=len(matrix[0])

    row=0
    col=cols-1
    while row<rows and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            col=col-1
        else:
            row=row+1
    return False

matrix = [ [1, 4, 7, 11, 15], 
          [2, 5, 8, 12, 19], 
          [3, 6, 9, 16, 22], 
          [10, 13, 14, 17, 24], 
          [18, 21, 23, 26, 30] ]
target=int(input("Enter the target value:"))
print(matrix_search(matrix,target))