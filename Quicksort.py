def swap(a,i,j):
    a[i],a[j]=a[j],a[i]
def partition(arr,l,h):
    pivot_pos=l
    pivot=arr[pivot_pos]
    i=l
    j=h
    while i<j :
        while i<j and arr[i]<=pivot:
            i=i+1
        while arr[j]>pivot:
            j=j-1
        if i<j:
            swap(arr,i,j)

    arr[pivot_pos],arr[j]=arr[j],arr[pivot_pos]
    return j

def quicksort(arr,l,h):
    if l<h:
        pi=partition(arr,l,h)
        print(pi)
        quicksort(arr,l,pi-1) #left partition
        quicksort(arr,pi+1,h) #right partition

a=[50,70,60,90,40,80,10,20,30]

# a=[1,2,3,4,5,6,7,8]
print(a)
quicksort(a,0,len(a)-1)
# x=partition(a)
print(a)


