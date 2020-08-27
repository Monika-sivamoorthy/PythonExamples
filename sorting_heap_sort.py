"""
Max and min heap construction
Sorting both ascending and descending using heap sort
"""


def max_heapify(arr, root, arr_len):
    # Note:
    # left_child = 2 * i,
    # right_child = 2 * i + 1

    left = (2 * root) + 1
    right = (2 * root) + 2

    largest = root
    if left < arr_len and arr[left] > arr[root]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        max_heapify(arr, largest, arr_len)


def min_heapify(arr, root, arr_len):
    left = (2 * root) + 1
    right = (2 * root) + 2

    smallest = root
    if left < arr_len and arr[left] < arr[root]:
        smallest = left
    if right < arr_len and arr[right] < arr[smallest]:
        smallest = right

    if smallest != root:
        arr[smallest], arr[root] = arr[root], arr[smallest]
        min_heapify(arr, smallest, arr_len)


def construct_max_heap(arr):
    # Note:
    # Heapify procedure can be applied to a node only when the children nodes are heapified.
    # Apply heapify to all the non-leaf nodes in a bottom-up manner.
    arr_len = len(arr)
    for index in range((arr_len // 2) - 1, -1, -1):
        max_heapify(arr, index, arr_len)
    return arr


def construct_min_heap(arr):
    arr_len = len(arr)
    for index in range((arr_len // 2) - 1, -1, -1):
        min_heapify(arr, index, arr_len)
    return arr


def heap_sort_asc(arr):
    len_arr = len(arr)
    for index in range(len_arr - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        max_heapify(arr, 0, index)
    return arr


def heap_sort_desc(arr):
    len_arr = len(arr)
    for index in range(len_arr - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        min_heapify(arr, 0, index)
    return arr


if __name__ == "__main__":
    input_arr = [4, 10, 3, 5, 1]
    min_heap = construct_min_heap([*input_arr])
    max_heap = construct_max_heap([*input_arr])
    sorted_asc = heap_sort_asc([*max_heap])
    sorted_desc = heap_sort_desc([*min_heap])

    print(f"Given:\n{input_arr}\n\n"
          f"Min-heap:\n{min_heap}\n"
          f"Max-heap:\n{max_heap}\n\n"
          f"Ascending:\n{sorted_asc}\n"
          f"Descending:\n{sorted_desc}")


# OUTPUT:
# ==================
#
# Given:
# [4, 10, 3, 5, 1]
#
# Min-heap:
# [1, 4, 3, 5, 10]
# Max-heap:
# [10, 5, 3, 4, 1]
#
# Ascending:
# [1, 3, 4, 5, 10]
# Descending:
# [10, 5, 4, 3, 1]
