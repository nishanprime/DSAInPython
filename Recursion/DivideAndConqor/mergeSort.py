def merge(arr1,arr2):
    temp=[]
    i=0
    j=0
    while (i<len(arr1)) and (j<len(arr2)):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i+=1
        else:
            temp.append(arr2[j])
            j+=1
    if(j<i):
        temp=temp+arr2[j:]
    if(i<j):
        temp=temp+arr1[i:]
    return temp

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=(len(arr))//2
    left=mergeSort(arr[0:mid])
    right=mergeSort(arr[mid:])
    return merge(left,right)

print(mergeSort([1,5,3,7,8,2,3,5]))



