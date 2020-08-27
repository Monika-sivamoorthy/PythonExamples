def linear_search(arr, n):
    for index, element in enumerate(arr):
        if element == n:
            return index
    return -1


def binary_search(arr, start, end, n):
    if start == end:
        return start if arr[start] == n else -1

    mid = (start + end) // 2
    return binary_search(arr, start, mid, n) if n <= arr[mid] else binary_search(arr, mid + 1, end, n)


if __name__ == "__main__":
    print("Note: Outputs -1 if element is not found in the array")

    unsorted_arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    to_find = 110
    print(f"\nLinear search:")
    print("----------------------------------------------------------------------")
    print(f"Array : {unsorted_arr}\nFind : {to_find}")
    position = linear_search(unsorted_arr, to_find)
    print(f"Element found at index: {position}")

    sorted_arr = [2, 3, 4, 10, 40]
    to_find = 10
    print(f"\nBinary search:")
    print("----------------------------------------------------------------------")
    print(f"Array : {sorted_arr}\nFind : {to_find}")
    position = binary_search(sorted_arr, 0, len(sorted_arr) - 1, to_find)
    print(f"Element found at index: {position}")

# OUTPUT:
# ====================================
#
# Note: Outputs -1 if element is not found in the array
#
# Linear search:
# ----------------------------------------------------------------------
# Array : [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# Find : 110
# Element found at index: 6
#
# Binary search:
# ----------------------------------------------------------------------
# Array : [2, 3, 4, 10, 40]
# Find : 10
# Element found at index: 3
