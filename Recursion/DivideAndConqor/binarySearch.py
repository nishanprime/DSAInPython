def BinarySearch(sortArr,left, right,target):
    print(left,right)
    if(left>right):
        return -1
    mid=(left+right)//2
    if(sortArr[mid]==target):
        return mid
    if target<sortArr[mid]:
        return BinarySearch(sortArr,0,mid-1,target)
    else:
        return BinarySearch(sortArr,mid+1,right,target)

print(BinarySearch([1,2,3,4,5,6,7],0,6,7))