import heapq


def KLargestElem(arr,k):
   # arr=[-elem for elem in arr]
   # print(arr)
   # heapq.heapify(arr)
   # for i in range(k-1):
   #     heapq.heappop(arr)
   # return -heapq.heappop(arr)
   hash={}
   array=[]
   for k in arr:
       if k not in hash:
           hash[k]=1
       else:
           hash[k]+=1
   for key,values in hash.items():
       array.append([key,values])
   return array

print(KLargestElem([4,2,9,7,5,6,7,1,3],2))