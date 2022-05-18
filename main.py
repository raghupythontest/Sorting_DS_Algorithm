def bubbleSort(a):
    print("Bubble sort:")
    for i in range(len(a) - 1):
        print(i)
        flag = 0
        for j in range(len(a) - i - 1):
            if a[j + 1] < a[j]:
                flag = 1
                a[j], a[j + 1] = a[j + 1], a[j]
        if flag == 0:
            break
    return a


def insertionSort(a):
    print("Insertion Sort:")
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j > -1 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
    return a


def selectionSort(a):
    print("Selection sort:")
    for i in range(len(a)):
        k = i
        for j in range(i + 1, len(a)):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
    return a


def merge(mylist, a, b):
    print("Merging:")
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            mylist[k] = a[i]
            i = i + 1
            k = k + 1
        else:
            mylist[k] = b[j]
            j = j + 1
            k = k + 1
    if i < len(a):
        for i in range(i, len(a)):
            mylist[k] = a[i]
            k = k + 1
    if j < len(b):
        for j in range(j, len(b)):
            mylist[k] = b[j]
            k = k + 1


def mergeSort(mylist):
    size = len(mylist)
    if size > 1:
        mid = size // 2
        left = mylist[:mid]
        right = mylist[mid:]
        mergeSort(left)
        mergeSort(right)
        # merge(mylist,left,right)
        left_size=len(left)
        right_size=len(right)
        print("Merging:")
        i = 0
        j = 0
        k = 0
        while i < left_size and j < right_size:
            if left[i] <= right[j]:
                mylist[k] = left[i]
                i = i + 1
                k = k + 1
            else:
                mylist[k] = right[j]
                j = j + 1
                k = k + 1
        while i < left_size:
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < right_size:
            mylist[k] = right[j]
            j += 1
            k += 1


# a = [1000,999,1001]
# print(bubbleSort(a))
# print(insertionSort(a))
# print(selectionSort(a))
b = [1000,999,1001]
# l = 0
# h = len(b) - 1
# mid = (l + h) // 2
mergeSort(b)
print(b)