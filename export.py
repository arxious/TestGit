def bubble_sort_optimized(arr):
    n = len(arr)
    swaps = 0
    passes = 0
    for p in range(n - 1):
        swapped = False
        for s in range(0, n - 1 - p):
            if arr[s] > arr[s + 1]:
                arr[s], arr[s + 1] = arr[s + 1], arr[s]
                swaps += 1
                swapped = True
        passes += 1
        if not swapped:  # already sorted; stop early (best case O(n))
            break
    return arr, passes, swaps

nums = [7, 6, 2, 4, 6, 7, 1, 8, 9]
sorted_nums, passes, swaps = bubble_sort_optimized(nums)
print(sorted_nums, f"(passes={passes}, swaps={swaps})")
