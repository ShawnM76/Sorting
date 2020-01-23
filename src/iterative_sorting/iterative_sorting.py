# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for num in range(i+1, len(arr)):
            if arr[smallest_index] > arr[num]:
                smallest_index = num
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap

    return arr


arr = [8, 4, 10, 5, 3, 1, 2]
# print(selection_sort(arr))
# TO-DO:  implement the Bubble Sort function below
# Need to do a while loop
# 4 loop inside of while loop
# check the index and number to the neighbor


def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for num in range(0, len(arr) - 1):
            if arr[num] > arr[num+1]:
                arr[num], arr[num+1] = arr[num+1], arr[num]
                flag = True
    return arr


print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
