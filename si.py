def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
result = binary_search(arr, target)

if result != -1:
    print("Target element is", target, "found at index", result)
else:
    print("Target element", target, "not found")
