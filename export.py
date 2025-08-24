def BubbleSort(arr):
    n = len(arr)
    passes = 0
    swaps = 0
    
    for p in range(n - 1):
        swapped = False
        for s in range(n - 1 - p):
            if arr[s] > arr[s + 1]:
                arr[s], arr[s + 1] = arr[s + 1], arr[s]
                swapped = True
                swaps += 1
        passes += 1
        
        if not swapped:
            print("List sorted!")
            break;

    return passes, swaps, arr

myArr = [6,7,3,1,2,9,8,7,0,3]

numPasses, numSwaps, sortedArray = BubbleSort(myArr)

print("Array sorted in: " + str(numPasses), "passes, and", + numSwaps, "swaps.")
print(myArr)
            
