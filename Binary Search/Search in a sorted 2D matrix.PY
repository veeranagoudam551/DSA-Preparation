def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    columns = len(matrix[0])
    low = 0
    high = rows * columns - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // columns
        cols = mid % columns

        if matrix[row][cols] == target:
            return (row, cols)
        elif matrix[row][cols] < target:
            low=mid +1
        else:
            high=mid -1
    return False




matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
target=int(input("Enter the target value:"))
print(matrix_search(matrix,target))