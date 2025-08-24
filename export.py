# I'll try doing bubble sort or something lol

int_array = [7,6,2,4,6,7,1,8,9]

def BubbleSort(arr):
    passes = 0
    swaps = 0
    for p in range(len(int_array)): # p = pass
        for s in range(len(int_array)): # Nested for loop n^2 complexity -- Worst time complexity but bear with me.
            if s != int_array.index(int_array[-1]) and (arr[s] > arr[s+1]):
                arr[s], arr[s+1] = arr[s+1], arr[s];
                swaps += 1
            elif s == int_array.index(int_array[-1]): # Reached the last element
                # start a new pass
                break;

        passes += 1
    
    print("Sorted in: " + str(passes) + " passes, and " + str(swaps), "swaps.")

    return arr

BubbleSort(int_array)

print(int_array)

