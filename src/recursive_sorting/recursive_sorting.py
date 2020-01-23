# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [None] * elements
    # TO-DO
    array1 = 0
    array2 = 0
    for index in range(elements):
        if array1 == len(arrA):
            merged_arr[index] = arrB[array2]
            array2 += 1
        elif array2 == len(arrB):
            merged_arr[index] = arrA[array1]
            array1 += 1
        elif arrA[array1] > arrB[array2]:
            merged_arr[index] = arrB[array2]
            array2 += 1
        else:
            merged_arr[index] = arrA[array1]
            array1 += 1

    # check next array and see if its greater or less than the current array
    # Then combined those two arrays and repeat until 1 array is left in order.

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    length = len(arr)
    if len(arr) > 1:
        x = length // 2
        # Divide the array in half
        arrA = merge_sort(arr[:x])
        arrB = merge_sort(arr[x:])
        arr = merge(arrA, arrB)
    # Then continue to keep dividing each individual array until each array
    # has either 1 element in it or none.
    # Then call merge.
    return arr


print(merge_sort([10, 100, 15, 13, 20, 8, 2, 7, 22, 24, 35, 99, 1]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
