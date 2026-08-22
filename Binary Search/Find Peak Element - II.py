#Time:  O(rows × log(cols))
#Space: O(1)

def find_peak(mat):
    rows = len(mat)
    cols = len(mat[0])

    low = 0
    high = cols - 1

    while low <= high:
        mid = (low + high) // 2

        # Find maximum element in mid column
        max_row = 0

        for row in range(rows):
            if mat[row][mid] > mat[max_row][mid]:
                max_row = row

        # Get left neighbour
        if mid - 1 >= 0:
            left = mat[max_row][mid - 1]
        else:
            left = -1

        # Get right neighbour
        if mid + 1 < cols:
            right = mat[max_row][mid + 1]
        else:
            right = -1

        # Check if it is a peak
        if mat[max_row][mid] > left and mat[max_row][mid] > right:
            return [max_row, mid]

        # Move towards the bigger neighbour
        elif left > mat[max_row][mid]:
            high = mid - 1

        else:
            low = mid + 1

    return [-1, -1]
            
mat=[[10, 12, 15], 
     [21, 13, 14], 
     [7, 16, 32]]
print(find_peak(mat))