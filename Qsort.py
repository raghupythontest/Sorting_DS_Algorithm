def qsort(array, low, high):
    if (low < high):
        pivot = low
        i = low
        j = high

        while (i < j):  # Main While Loop
            while array[i] <= array[pivot] and i < high:  # While Loop "i"
                i += 1
            while array[j] > array[pivot]:  # While Loop "j"
                j -= 1

            if (i < j):
                array[i], array[j] = array[j], array[i]

        array[pivot], array[j] = array[j], array[pivot]
        qsort(array, low, j - 1)
        qsort(array, j + 1, high)
        return array
a=[50,70,60,90,40,80,10,20,30]
print(qsort(a,0,len(a)-1))