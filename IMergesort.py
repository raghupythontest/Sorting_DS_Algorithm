def merge(arr,l,m,h):
    i=l
    j=m+1
    k=l
    while i<=m and j<=h:
        if arr[i] < arr[j]:
            arr[k]=arr[i]
            k+=1
            i+=1
        else:
            arr[k] = arr[j]
            k += 1
            j += 1
    while i<=m:
        arr[k]=arr[i]
        k+=1
        i+=1
    while i<=h:
        arr[k]=arr[j]
        k+=1
        j+=1




# def Imergesort(arr):
#     p=2
#     while p <=len(arr):
#         i=0
#         while (i+p-1) < len(arr):
#             l=i
#             h=i+p-1
#             mid=(l+h)//2
#             merge(arr,l,mid,h)
#             i=i+p
#
#         p=p*2
#
a=[8,3,7,4,9,2,6,5]
print(a)
merge(a,0,3,7)
print(a)