def bubble_sort(arr):
    print("\nBubble sort :")
    print("----------------------------------------------------------------------")
    len_arr = len(arr)

    for i in range(len_arr):

        swapped = False

        for index in range(len_arr - i - 1):
            if arr[index] > arr[index + 1]:
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

        print(f"Pass {i}: {arr}")

        if not swapped:
            break


def selection_sort(arr):
    print("\nSelection sort :")
    print("----------------------------------------------------------------------")
    len_arr = len(arr)

    for i in range(len_arr):

        minimum = i

        for index in range(i, len_arr):
            if arr[index] < arr[minimum]:
                minimum = index

        arr[i], arr[minimum] = arr[minimum], arr[i]

        print(f"Pass {i}: {arr}")


def insertion_sort(arr):
    print("\nInsertion sort :")
    print("----------------------------------------------------------------------")
    len_arr = len(arr)

    for i in range(1, len_arr):

        element = arr[i]

        for index in range(i - 1, -1, -1):
            if arr[index] > element:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
            else:
                arr[index + 1] = element

        print(f"Pass {i}: {arr}")


if __name__ == "__main__":

    input_arr = [64, 25, 12, 22, 11]
    print(f"\nInput array: {input_arr}")

    bubble_sort([*input_arr])
    selection_sort([*input_arr])
    insertion_sort([*input_arr])


# OUTPUT:
# ===============================
#
# Input array: [64, 25, 12, 22, 11]
#
# Bubble sort :
# ----------------------------------------------------------------------
# Pass 0: [25, 12, 22, 11, 64]
# Pass 1: [12, 22, 11, 25, 64]
# Pass 2: [12, 11, 22, 25, 64]
# Pass 3: [11, 12, 22, 25, 64]
# Pass 4: [11, 12, 22, 25, 64]
#
# Selection sort :
# ----------------------------------------------------------------------
# Pass 0: [11, 25, 12, 22, 64]
# Pass 1: [11, 12, 25, 22, 64]
# Pass 2: [11, 12, 22, 25, 64]
# Pass 3: [11, 12, 22, 25, 64]
# Pass 4: [11, 12, 22, 25, 64]
#
# Insertion sort :
# ----------------------------------------------------------------------
# Pass 1: [25, 64, 12, 22, 11]
# Pass 2: [12, 25, 64, 22, 11]
# Pass 3: [12, 22, 25, 64, 11]
# Pass 4: [11, 12, 22, 25, 64]
#
