# Implementation of Binary Search Tree, It is suitable for Sorted list

def binarySearch(arr,l,h,key):
    if l<=h:
        mid = (l + h) // 2
        if key==arr[mid]:
            return mid
        elif key>mid:
            return binarySearch(arr,l=mid+1,h=h,key=key)
        else:
            return binarySearch(arr,l=l,h=mid-1,key=key)
a=[1,2,3,4,5,6,7,8]
l=0
h=len(a)-1
print(binarySearch(a,l,h,6))