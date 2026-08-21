def student_count(arr, mid):
    student = 1
    current_pages = 0

    for i in range(len(arr)):

        if current_pages + arr[i] > mid:

            student = student + 1
            current_pages = arr[i]

        else:
            current_pages += arr[i]
    return student

def find_pages(arr, n, k):
    if n < k:
        return -1

    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low + high) // 2
        students = student_count(arr, mid)

        if students > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [12, 34, 67, 90]
n = len(arr)
k = int(input("Enter the number of students: "))
print(find_pages(arr, n, k))