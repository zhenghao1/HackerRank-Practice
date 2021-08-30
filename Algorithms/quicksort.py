def partition(arr, low, high):
    item = low - 1

    # Take last element as pivot
    pivot = arr[high]

    # Range is 0 to the second last element,
    # Since last element is picked as pivot already
    for i in range(low, high):
        if(arr[i] <= pivot):
            item += 1
            arr[item], arr[i] = arr[i], arr[item]

    # After for loop has ended, value of item will be the
    # index just before the item that is greater than pivot

    # We need to swap the first element that is greater than pivot with pivot
    arr[item+1], arr[high] = arr[high], arr[item+1]
    return item+1

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

# Find k smallest
def quickselect_smallest(arr, low, high, k):
    if (k > 0 and k <= high - low + 1):
        pivot = partition(arr, low, high)

        # eg, k=4 means 4th largest, also means it is in index 3
        #
        # By this time, elements to the left of pivot is smaller than pivot and
        # right of pivot is greater than pivot
        #
        # So if pivot just so happens to be 3, that means 4th largest will be at pivot
        if (pivot - low == k - 1):
            return arr[pivot]

        # If kth position is more, recur for left subarray
        if (pivot - low > k - 1):
            return quickselect_smallest(arr, low, pivot-1, k)

        # Else recur right subarray
        return quickselect_smallest(arr, pivot+1, high, k-pivot+low-1)



if __name__ == '__main__':
    arr = [3, 2, 1, 9, 8, 7, 6, 5]
    arr2 = [3, 2, 1, 9, 8, 7, 6, 5]
    l = 0
    r = len(arr) - 1
    print(f"Original array: {arr}")
    quicksort(arr, l, r)
    print(f"Sorted array: {arr}")
    print("-" * 30)
    print(f"Original array: {arr2}")
    value = quickselect_smallest(arr2, l, r, 3)
    print(f"Third smallest is: {value}")


