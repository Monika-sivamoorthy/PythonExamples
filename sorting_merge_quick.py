"""
Both quick and merge sort follows divide and conquer paradiagram
"""


def merge_sub_arrays(first, second):
    new_arr = []
    print(f"Merge : {first}, {second}")

    while len(first) and len(second):
        if first[0] < second[0]:
            new_arr.append(first.pop(0))
        else:
            new_arr.append(second.pop(0))

    if len(first):
        new_arr.extend(first)
    else:
        new_arr.extend(second)

    print(f"{new_arr}")
    return new_arr


def merge_sort(arr, start, end):
    if start == end:
        return [arr[start]]

    mid = (start + end) // 2
    left = merge_sort(arr, start, mid)
    right = merge_sort(arr, mid + 1, end)

    return merge_sub_arrays(left, right)


def get_partition_position(arr, start, end):
    pivot = arr[start]
    lesser = start
    greater = end
    while lesser < greater:
        while arr[lesser] <= pivot and lesser < end:
            lesser += 1

        while arr[greater] >= pivot and greater > start:
            greater -= 1

        if lesser < greater:
            arr[lesser], arr[greater] = arr[greater], arr[lesser]

    arr[greater], arr[start] = arr[start], arr[greater]
    print(f"Pivot position : {greater}, {arr}")

    return greater


def quick_sort(arr, start, end):
    if start < end:
        partition = get_partition_position(arr, start, end)
        quick_sort(arr, start, partition)
        quick_sort(arr, partition + 1, end)
    return arr


if __name__ == "__main__":
    input_arr = [10, 80, 30, 90, 40, 50, 70]
    print(f"\nInput array: {input_arr}")

    print(f"\nMerge sort :")
    print("----------------------------------------------------------------------")
    merge_sort(input_arr, 0, len(input_arr) - 1)

    print(f"\nQuick sort :")
    print("----------------------------------------------------------------------")
    quick_sort(input_arr, 0, len(input_arr) - 1)


# OUTPUT:
# ===============================
#
# Input array: [10, 80, 30, 90, 40, 50, 70]
#
# Merge sort :
# ----------------------------------------------------------------------
# Merge : [10], [80]
# [10, 80]
# Merge : [30], [90]
# [30, 90]
# Merge : [10, 80], [30, 90]
# [10, 30, 80, 90]
# Merge : [40], [50]
# [40, 50]
# Merge : [40, 50], [70]
# [40, 50, 70]
# Merge : [10, 30, 80, 90], [40, 50, 70]
# [10, 30, 40, 50, 70, 80, 90]
#
# Quick sort :
# ----------------------------------------------------------------------
# Pivot position : 0, [10, 80, 30, 90, 40, 50, 70]
# Pivot position : 5, [10, 50, 30, 70, 40, 80, 90]
# Pivot position : 3, [10, 40, 30, 50, 70, 80, 90]
# Pivot position : 2, [10, 30, 40, 50, 70, 80, 90]
# Pivot position : 1, [10, 30, 40, 50, 70, 80, 90]
# Pivot position : 4, [10, 30, 40, 50, 70, 80, 90]
