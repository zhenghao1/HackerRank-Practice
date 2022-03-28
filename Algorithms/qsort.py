def partition(arr, l, h):
    item = l - 1
    pivot = arr[h]
    for i in range(l, h):
        if(arr[i] <= pivot):
            arr[item], arr[i] = arr[i], arr[item]
    arr[item+1], arr[h] = arr[h], arr[item+1]
    return item+1

def quicksort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quicksort(arr, l, pivot-1)
        quicksort(arr, pivot+1, h)
